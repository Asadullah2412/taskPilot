import uuid
from collections.abc import Sequence
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from database.schemas import TaskCreate,updateTask,deleteTask
from database.model import Task

from database.dependencies import db_dependency

# creating a new task
async def create_task(data:TaskCreate,db=db_dependency):
    # check
    if db.scalers(select(Task).where(Task.title == data.title)).first():
        return "Task is already present"

    task = Task(title=data.title,description=data.description)
    db.add(task)
    db.commit()
    db.refresh(task)
    return task


# Reading all tasks
async def read_task(db:db_dependency):
    tasks = db.scalars(select(Task)).all()
    return tasks

# updating tasks
async def update_task(data:updateTask,db:db_dependency):
    task = db.get(Task,data.title)
    if not task:
        return "task not found"

    task.completed = data.completed


# delete task
async def delete_task(data:deleteTask,db:db_dependency):
    task = db.get(Task,data.title)

    if not task:
        return "task is not present"

    db.delete(task)
    db.commit()
    return None


