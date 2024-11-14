from pydantic import BaseModel
from datetime import datetime


class NewsBase(BaseModel):
    title: str
    text: str


class NewsRead(NewsBase):
    uuid: str
    created_at: datetime
    updated_at: datetime


class NewsCreate(NewsBase):
    pass


class NewsUpdate(NewsCreate):
    pass
