from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime


class Comment(BaseModel):
    id: int
    news_id: int
    title: str
    date: datetime
    comment: str


class News(BaseModel):
    id: int
    title: str
    date: datetime
    body: str
    deleted: bool
    comments_count: Optional[int] = 0
    comments: Optional[List[Comment]] = []


class NewsList(BaseModel):
    news: List[News]
    news_count: int


class CreateNews(BaseModel):
    title: str
    date: datetime
    body: str


class CreateComment(BaseModel):
    news_id: int
    title: str
    comment: str
