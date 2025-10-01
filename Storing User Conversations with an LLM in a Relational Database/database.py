from sqlalchemy.ext.asyncio import create_async_engine
from entities import Base

database_url = (
    "postgresql+psycopg://fastapi:mysecretpassword@localhost:5432/backend_db"
) # 1. Database URL for PostgreSQL

engine = create_async_engine(database_url, echo=True) # 2. Create async engine

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all) # Drop all tables (for development/testing)
        await conn.run_sync(Base.metadata.create_all) # 3. Create all tables