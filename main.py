from fastapi import FastAPI
from models import Base
from database import engine
from crud import task_router

app = FastAPI()

app.include_router(task_router)

Base.metadata.create_all(engine)

