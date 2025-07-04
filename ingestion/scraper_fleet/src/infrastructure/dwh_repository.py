from typing import List
from domain.reel import Reel
from domain.abstract_repository import AbstractReelRepository
from config import config
from sqlalchemy import create_engine, Table, Column, String, Integer, MetaData, DateTime
from sqlalchemy.engine import Engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.sql import select
from datetime import datetime

class DWHReelRepository(AbstractReelRepository):
    """
    Репозиторий для хранения рилсов в DWH (PostgreSQL через SQLAlchemy).
    """
    def __init__(self, dsn: str = None, table: str = None) -> None:
        self._dsn = dsn or config.dwh.dsn
        self._table_name = table or config.dwh.table
        self._engine: Engine = create_engine(self._dsn)
        self._metadata = MetaData()
        self._table = Table(
            self._table_name, self._metadata,
            Column("id", String, primary_key=True),
            Column("author", String),
            Column("description", String),
            Column("likes", Integer),
            Column("views", Integer),
            Column("url", String),
            Column("posted_at", DateTime),
        )
        self._metadata.create_all(self._engine)

    def save(self, reel: Reel) -> None:
        with self._engine.begin() as conn:
            data = reel.dict()
            # Преобразуем posted_at к datetime, если это строка
            if isinstance(data["posted_at"], str):
                data["posted_at"] = datetime.fromisoformat(data["posted_at"].replace("Z", "+00:00"))
            # UPSERT (PostgreSQL >=9.5)
            insert_stmt = self._table.insert().values(**data)
            upsert_stmt = insert_stmt.on_conflict_do_update(
                index_elements=["id"],
                set_=data
            )
            conn.execute(upsert_stmt)

    def get_all(self) -> List[Reel]:
        with self._engine.connect() as conn:
            result = conn.execute(select(self._table))
            rows = result.fetchall()
            return [
                Reel(
                    id=row["id"],
                    author=row["author"],
                    description=row["description"],
                    likes=row["likes"],
                    views=row["views"],
                    url=row["url"],
                    posted_at=row["posted_at"],
                )
                for row in rows
            ] 