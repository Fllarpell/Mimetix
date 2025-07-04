import json
from typing import List
import boto3
from botocore.exceptions import ClientError
from domain.reel import Reel
from domain.abstract_repository import AbstractReelRepository
from config import config

class S3ReelRepository(AbstractReelRepository):
    """
    Реализация AbstractReelRepository для хранения метаданных рилсов в S3 (Data Lake).
    Каждый рилс сохраняется как отдельный JSON-объект по ключу reels/{reel_id}.json
    """
    def __init__(self, bucket: str = None, prefix: str = None) -> None:
        self._bucket = bucket or config.s3.bucket
        self._prefix = prefix or config.s3.prefix
        self._s3 = boto3.client(
            "s3",
            aws_access_key_id=config.s3.access_key,
            aws_secret_access_key=str(config.s3.secret_key) if config.s3.secret_key else None,
            region_name=config.s3.region,
            endpoint_url=config.s3.endpoint_url
        )

    def save(self, reel: Reel) -> None:
        key = f"{self._prefix}{reel.id}.json"
        data = reel.json(ensure_ascii=False)
        self._s3.put_object(Bucket=self._bucket, Key=key, Body=data.encode("utf-8"), ContentType="application/json")

    def get_all(self) -> List[Reel]:
        reels = []
        paginator = self._s3.get_paginator("list_objects_v2")
        for page in paginator.paginate(Bucket=self._bucket, Prefix=self._prefix):
            for obj in page.get("Contents", []):
                key = obj["Key"]
                try:
                    response = self._s3.get_object(Bucket=self._bucket, Key=key)
                    data = response["Body"].read().decode("utf-8")
                    reels.append(Reel.parse_raw(data))
                except (ClientError, json.JSONDecodeError, TypeError, ValueError):
                    continue
        return reels 