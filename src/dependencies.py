from typing import Annotated
from fastapi import Depends, HTTPException, Path, status
from uuid import uuid4

from src.schemas import NewsRead
from src.service import NewsService


error_found = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail=f'User not found',
)


def valid_news_id(
    news_id: Annotated[uuid4, Path], service: Annotated[NewsService, Depends()]
) -> NewsRead | None:
    news = service.get_news_by_id(news_id)

    if not news:
        raise error_found

    return news


def get_newses(service: Annotated[NewsService, Depends()]) -> list[NewsRead]:
    newses = service.get_newses()
    return newses
