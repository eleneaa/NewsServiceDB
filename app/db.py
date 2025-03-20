from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from databases import Database
from sqlalchemy import MetaData


DATABASE_URL = "sqlite+aiosqlite:///./news.db"

engine = create_async_engine(DATABASE_URL, echo=True)

async_session = sessionmaker(
                bind=engine,
                autocommit=False,
                autoflush=False,
                class_=AsyncSession)

database = Database(DATABASE_URL)

metadata = MetaData()
