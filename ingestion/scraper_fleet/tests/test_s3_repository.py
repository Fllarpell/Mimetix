import pytest
from moto import mock_s3
import boto3
from infrastructure.s3_repository import S3ReelRepository
from domain.reel import Reel
from botocore.exceptions import EndpointConnectionError
from datetime import datetime

@mock_s3
def test_s3_reel_repository_save_and_get_all():
    bucket = "test-bucket"
    s3 = boto3.client("s3")
    s3.create_bucket(Bucket=bucket)
    repo = S3ReelRepository(bucket=bucket, prefix="test-reels/")
    reel = Reel(
        id="123",
        author="test_author",
        description="desc",
        likes=10,
        views=100,
        url="http://example.com",
        posted_at=datetime(2024, 1, 1, 0, 0, 0)
    )
    repo.save(reel)
    reels = repo.get_all()
    assert len(reels) == 1
    assert reels[0].id == "123"
    assert reels[0].author == "test_author"
    assert isinstance(reels[0].posted_at, datetime)
    assert reels[0].posted_at == datetime(2024, 1, 1, 0, 0, 0)

@mock_s3
def test_s3_reel_repository_empty_bucket():
    bucket = "test-bucket"
    s3 = boto3.client("s3")
    s3.create_bucket(Bucket=bucket)
    repo = S3ReelRepository(bucket=bucket, prefix="empty/")
    reels = repo.get_all()
    assert reels == []

@mock_s3
def test_s3_reel_repository_connection_error(monkeypatch):
    bucket = "test-bucket"
    s3 = boto3.client("s3")
    s3.create_bucket(Bucket=bucket)
    repo = S3ReelRepository(bucket=bucket, prefix="test/")
    def fail_connect(*a, **kw):
        raise EndpointConnectionError(endpoint_url="https://s3.amazonaws.com")
    monkeypatch.setattr(repo._s3, "get_object", fail_connect)
    with pytest.raises(EndpointConnectionError):
        repo.get_all() 