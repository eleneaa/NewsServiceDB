from datetime import datetime, timezone
from sqlalchemy import Table, Column, Integer, String, Boolean, ForeignKey, DateTime
from app.db import metadata


comment_table = Table(
    "comments",
    metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("news_id", Integer, ForeignKey("news.id"), nullable=False),
    Column("title", String, nullable=False),
    Column("date", DateTime, nullable=False, default=datetime.now(timezone.utc)),
    Column("comment", String, nullable=False),
)


news_table = Table(
    "news",
    metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("title", String, nullable=False),
    Column("date", DateTime, nullable=False, default=datetime.now(timezone.utc)),
    Column("body", String, nullable=False),
    Column("deleted", Boolean, default=False),
)
