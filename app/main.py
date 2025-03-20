from fastapi import FastAPI

from .db import engine, metadata
from .routes import news

app = FastAPI()

app.include_router(news.router, prefix="/api", tags=["news"])


@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(metadata.create_all)


@app.on_event("shutdown")
async def shutdown():
    await engine.dispose()


@app.get("/")
async def root():
    return {"message": "｡ ₊°༺❤︎༻°₊ ｡ Welcome to the News API, sweetie! ｡ ₊°༺❤︎༻°₊ ｡"}
