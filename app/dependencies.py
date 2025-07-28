
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from fastapi import Depends
from app.config import get_settings

_engine = create_async_engine(get_settings().database_url, echo=False)
_Session = async_sessionmaker(_engine, expire_on_commit=False)

async def get_db() -> AsyncSession:
    async with _Session() as session:
        yield session
