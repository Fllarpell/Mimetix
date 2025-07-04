import sqlite3
from typing import List
from domain.reel import Reel
from domain.abstract_repository import AbstractReelRepository
from config import config

class SQLiteReelRepository(AbstractReelRepository):
    """Реализация AbstractReelRepository для хранения рилсов в SQLite."""

    def __init__(self, db_path: str = None) -> None:
        self._db_path = db_path or config.sqlite_path
        self._init_db()

    def _init_db(self) -> None:
        with sqlite3.connect(self._db_path) as conn:
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS reels (
                    id TEXT PRIMARY KEY,
                    author TEXT,
                    description TEXT,
                    likes INTEGER,
                    views INTEGER,
                    url TEXT,
                    posted_at TEXT
                )
                """
            )

    def save(self, reel: Reel) -> None:
        with sqlite3.connect(self._db_path) as conn:
            conn.execute(
                """
                INSERT OR REPLACE INTO reels (id, author, description, likes, views, url, posted_at)
                VALUES (?, ?, ?, ?, ?, ?, ?)
                """,
                (reel.id, reel.author, reel.description, reel.likes, reel.views, reel.url, reel.posted_at)
            )

    def get_all(self) -> List[Reel]:
        with sqlite3.connect(self._db_path) as conn:
            rows = conn.execute("SELECT id, author, description, likes, views, url, posted_at FROM reels").fetchall()
            return [
                Reel(
                    id=row[0],
                    author=row[1],
                    description=row[2],
                    likes=row[3],
                    views=row[4],
                    url=row[5],
                    posted_at=row[6],
                )
                for row in rows
            ] 