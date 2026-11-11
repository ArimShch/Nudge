from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.pool import AsyncAdaptedQueuePool

from contextlib import asynccontextmanager
from collections.abc import AsyncIterator

from ..core.config import settings

db_url = settings.get_db_url()

engine = create_async_engine(
    url=db_url,
    pool_size=15,
    max_overflow=25,
    pool_pre_ping=True, 
    pool_recycle=1800, 
)

session_factory = async_sessionmaker(
    bind=engine,
    expire_on_commit=False,
    autoflush=False,
)


@asynccontextmanager
async def session_scope() -> AsyncIterator[AsyncSession]:
    async with session_factory() as session:
        async with session.begin():
            yield session


async def get_session() -> AsyncIterator[AsyncSession]:
    async with session_scope() as session:
        yield session