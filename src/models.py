from sqlalchemy import String, func, Uuid
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from clickhouse_sqlalchemy import engines
from src.database import DATABASE
import uuid
from datetime import datetime


class Base(DeclarativeBase):
    pass


class News(Base):
    __tablename__ = 'newses'
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
