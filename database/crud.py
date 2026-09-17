from sqlalchemy.orm import Session
from sqlalchemy import select
from database.schemas import TaskCreate, updateTask, deleteTask
from database.model import Task

# Creating a new task
def create_task(data: TaskCreate, db: Session):
    existing_task = db.scalars(
        select(Task).where(Task.title == data.title)
    ).first()

    if existing_task:
        return {
            "success": False,
            "error": "TASK_ALREADY_EXISTS",
            "task_id": str(existing_task.id),
            "title": existing_task.title
        }

    task = Task(
        title=data.title,
        description=data.description
    )

    db.add(task)
    db.commit()
    db.refresh(task)

    return {
        "success": True,
        "task_id": str(task.id),
        "title": task.title,
        "description": task.description,
        "completed": task.completed
    }


# Reading all tasks
def read_tasks(db: Session):
    # Pure synchronous call
    return db.scalars(select(Task)).all()


# Updating tasks
def update_task(data: updateTask, db: Session):
    task = db.query(Task).filter(Task.id == data.id).first()
    if not task:
        return "task not found"

    task.completed = data.completed
    db.commit()
    return True


# Delete task
def delete_task(data: deleteTask, db: Session):
    task = db.query(Task).filter(Task.id == data.id).first()
    if not task:
        return "task is not present"

    db.delete(task)
    db.commit()
    return True
