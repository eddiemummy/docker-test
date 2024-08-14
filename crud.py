from fastapi import APIRouter, Depends
from database import get_db
from models import Task
from sqlalchemy.orm import Session
from schemas import CreateTask


task_router = APIRouter(
    prefix="/tasks",
    tags=["tasks"],
    responses={404: {"description": "Not found"}},
)

@task_router.get("/")
async def read_tasks(db: Session = Depends(get_db)):
    tasks = db.query(Task).all()
    return tasks



@task_router.post("/")
async def create_task(task: CreateTask, db: Session = Depends(get_db)):
    db_task = Task(**task.model_dump())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task
