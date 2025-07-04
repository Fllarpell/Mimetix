from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class Reel(BaseModel):
    """
    Сущность Instagram Reel (domain entity, pydantic-схема).
    """
    id: str = Field(..., description="Уникальный идентификатор рилса")
    author: str = Field(..., description="Автор рилса")
    description: str = Field(..., description="Описание")
    likes: int = Field(..., description="Количество лайков")
    views: int = Field(..., description="Количество просмотров")
    url: str = Field(..., description="Ссылка на видео")
    posted_at: datetime = Field(..., description="Дата публикации (datetime)")
    # Можно добавить больше полей по мере необходимости 