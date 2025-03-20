from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, HTTPException, Depends

from app.db import async_session
from app.models import news_table, comment_table
from app.schemas import CreateNews, CreateComment

router = APIRouter()


async def get_db():
    async with async_session() as session:
        yield session


@router.get("/")
async def get_all_news(db: AsyncSession = Depends(get_db)):
    news_list = news_table.select().where(news_table.c.deleted == False)
    result = await db.execute(news_list)
    news = result.fetchall()

    news_count = len(news)

    return {"news": [{"id": row.id,
                      "title": row.title,
                      "date": row.date,
                      "body": row.body,
                      "deleted": row.deleted} for row in news],
            "news_count": news_count}


@router.get("/news/{news_id}")
async def get_news_by_id(news_id: int, db: AsyncSession = Depends(get_db)):
    current_news = news_table.select().where(news_table.c.id == news_id)
    news_result = await db.execute(current_news)
    news = news_result.fetchone()

    if news is None:
        raise HTTPException(status_code=404, detail=f"News with id={news_id} not found")

    if news.deleted:
        raise HTTPException(status_code=404, detail=f"News with id={news_id} delete")

    comments_query = comment_table.select().where(comment_table.c.news_id == news_id)
    comments_result = await db.execute(comments_query)
    comments = comments_result.fetchall()

    comments_formatted = [
        {
            "id": comment.id,
            "news_id": comment.news_id,
            "title": comment.title,
            "date": comment.date,
            "comment": comment.comment,
        }
        for comment in comments
    ]

    comments_count = len(comments)

    return {
        "id": news.id,
        "title": news.title,
        "date": news.date,
        "body": news.body,
        "deleted": news.deleted,
        "comments": comments_formatted,
        "comments_count": comments_count,
    }



@router.post("/news")
async def create_news(
        news_data: CreateNews,
        db: AsyncSession = Depends(get_db), ):
    query = news_table.insert().values(**news_data.dict(exclude_unset=True), deleted=False)
    result = await db.execute(query)
    await db.commit()

    return {
        "id": result.lastrowid,
        "title": news_data.title,
        "body": news_data.body,
        "date": news_data.date
    }


@router.post("/comment")
async def create_comment(
        comment_data: CreateComment,
        db: AsyncSession = Depends(get_db), ):
    query = comment_table.insert().values(comment_data.dict(exclude_unset=True))
    result = await db.execute(query)
    await db.commit()

    return {
        "id": result.lastrowid,
        "title": comment_data.title,
        "comment": comment_data.comment,
        "news_id": comment_data.news_id
    }
