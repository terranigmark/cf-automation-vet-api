import asyncio
from sqlalchemy.ext.asyncio import create_async_engine
from app.config import get_settings
from app.models import Base

async def init_models():
    engine = create_async_engine(get_settings().database_url, echo=True)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

if __name__ == "__main__":
    asyncio.run(init_models())
