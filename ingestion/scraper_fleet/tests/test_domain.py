import pytest
from src.domain.reel import Reel
from src.domain.repository import ReelRepository

class DummyReelRepository(ReelRepository):
    def __init__(self):
        self._data = []
    def save(self, reel: Reel) -> None:
        self._data.append(reel)
    def get_all(self):
        return self._data

def test_reel_entity():
    reel = Reel(
        id="123",
        author="test_author",
        description="desc",
        likes=10,
        views=100,
        url="http://example.com",
        posted_at="2024-01-01T00:00:00Z"
    )
    assert reel.id == "123"
    assert reel.likes == 10

def test_reel_repository():
    repo = DummyReelRepository()
    reel = Reel(
        id="1",
        author="a",
        description="d",
        likes=1,
        views=2,
        url="u",
        posted_at="2024-01-01T00:00:00Z"
    )
    repo.save(reel)
    assert repo.get_all() == [reel] 