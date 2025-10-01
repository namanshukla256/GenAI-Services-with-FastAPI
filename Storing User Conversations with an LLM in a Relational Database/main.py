from contextlib import asynccontextmanager
from fastapi import FastAPI
from database import engine, init_db

@asynccontextmanager
async def lifespan(_: FastAPI):
    await init_db() # Initialize the database
    yield # Application runs
    await engine.dispose() # Dispose of the engine on shutdown

app = FastAPI(lifespan=lifespan)