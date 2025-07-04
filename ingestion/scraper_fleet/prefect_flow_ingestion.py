from prefect import flow, task, get_run_logger
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))
from main import main as ingestion_main

# Slack алерт (пример)
def send_slack_alert(msg: str):
    import requests
    webhook_url = os.getenv("SLACK_WEBHOOK_URL")
    if webhook_url:
        requests.post(webhook_url, json={"text": msg})

@task(retries=2, retry_delay_seconds=600)
def run_ingestion():
    logger = get_run_logger()
    logger.info("Запуск ingestion pipeline...")
    try:
        ingestion_main()
        logger.info("Ingestion pipeline завершён.")
    except Exception as e:
        logger.error(f"Ошибка: {e}")
        send_slack_alert(f"Prefect flow failed: {e}")
        raise

@flow(name="scraper-fleet-ingestion-flow")
def scraper_fleet_flow():
    run_ingestion()

if __name__ == "__main__":
    scraper_fleet_flow() 