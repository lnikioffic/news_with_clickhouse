from sqlalchemy import UniqueConstraint, func, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from clickhouse_sqlalchemy import engines
from src.database import DATABASE
import uuid
from datetime import datetime


class Base(DeclarativeBase):
    pass


class News(Base):
    __tablename__ = 'news'
    __table_args__ = (
        engines.MergeTree(order_by=['uuid']),
        {'schema': DATABASE},
    )

    uuid: Mapped[str] = mapped_column(primary_key=True)
    title: Mapped[str]
    text: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(
        server_default=func.now(), onupdate=func.now()
    )


class Tags(Base):
    __tablename__ = 'tags'
    __table_args__ = (
        engines.MergeTree(order_by=['uuid']),
        {'schema': DATABASE},
    )
    uuid: Mapped[str] = mapped_column(primary_key=True)
    name: Mapped[str]


class News_Tags(Base):
    __tablename__ = 'news_tags'
    __table_args__ = (
        engines.MergeTree(order_by=['news_uuid']),
        {'schema': DATABASE},
    )
    news_uuid: Mapped[str] = mapped_column(ForeignKey('news.uuid'), primary_key=True)
    tags_uuid: Mapped[str] = mapped_column( ForeignKey('tags.uuid'), primary_key=True)
