from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))
from main import main as ingestion_main

# Email алерты
ALERT_EMAILS = [os.getenv("ALERT_EMAIL", "alerts@example.com")]

# Slack алерт через webhook (пример)
def slack_alert(context):
    import requests
    webhook_url = os.getenv("SLACK_WEBHOOK_URL")
    if webhook_url:
        msg = f"Airflow DAG Failed: {context['task_instance'].dag_id} ({context['task_instance'].task_id})"
        requests.post(webhook_url, json={"text": msg})

def run_ingestion(**context):
    ingestion_main()

with DAG(
    dag_id="scraper_fleet_ingestion",
    start_date=datetime(2024, 1, 1),
    schedule_interval="@daily",
    catchup=False,
    max_active_runs=1,
    default_args={
        "retries": 2,
        "retry_delay": timedelta(minutes=10),
        "owner": "data-eng",
        "email": ALERT_EMAILS,
        "email_on_failure": True,
        "email_on_retry": True,
        "on_failure_callback": slack_alert,
    },
    tags=["reels", "ingestion", "scraper_fleet"],
) as dag:
    ingest_task = PythonOperator(
        task_id="run_ingestion_pipeline",
        python_callable=run_ingestion,
        provide_context=True,
    ) 