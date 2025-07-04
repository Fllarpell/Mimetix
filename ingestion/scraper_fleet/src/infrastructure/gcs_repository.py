from typing import List
from google.cloud import storage
from domain.reel import Reel
from domain.abstract_repository import AbstractReelRepository
from config import config
import json

class GCSReelRepository(AbstractReelRepository):
    """
    Репозиторий для хранения рилсов в Google Cloud Storage (GCS).
    Каждый рилс сохраняется как отдельный JSON-объект по ключу reels/{reel_id}.json
    """
    def __init__(self, bucket: str = None, prefix: str = None) -> None:
        self._bucket = bucket or config.gcs.bucket
        self._prefix = prefix or config.gcs.prefix
        self._client = storage.Client.from_service_account_json(config.gcs.credentials_path) if config.gcs.credentials_path else storage.Client()
        self._bucket_obj = self._client.bucket(self._bucket)

    def save(self, reel: Reel) -> None:
        key = f"{self._prefix}{reel.id}.json"
        blob = self._bucket_obj.blob(key)
        data = reel.json(ensure_ascii=False)
        blob.upload_from_string(data, content_type="application/json")

    def get_all(self) -> List[Reel]:
        reels = []
        blobs = self._client.list_blobs(self._bucket, prefix=self._prefix)
        for blob in blobs:
            try:
                data = blob.download_as_text()
                reels.append(Reel.parse_raw(data))
            except (json.JSONDecodeError, ValueError):
                continue
        return reels 