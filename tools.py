from langchain_core.tools import tool
from database.crud import create_task, delete_task, update_task, read_tasks
from database.schemas import TaskCreate, deleteTask, updateTask
# Import your synchronous SessionLocal factory
from database.database_setup import SessionLocal 

@tool
def newTask(title: str, description: str):
    """
    Add a new task.
    """

    with SessionLocal() as db:
        newTask_data = TaskCreate(
            title=title,
            description=description
        )

        return create_task(
            data=newTask_data,
            db=db
        )

@tool 
def readTasks():
    """
        Reads all the tasks from the database. 
        Returns data formatted strictly as: - Title: Description (Completed: True/False)
        """
    with SessionLocal() as db:
        tasks = read_tasks(db=db)
        
    
    task_strings = [
       {
           "id": str(t.id),
           "title": t.title,
           "description": t.description,
           "completed": t.completed
       }
       for t in tasks
   ]
    return task_strings





@tool
def TaskUpdate(title: str, completed: bool):
    """
    Updates task as completed as True or False
    """
    with SessionLocal() as db:
        task_data = updateTask(title=title, completed=completed)
        result = update_task(data=task_data, db=db)
        
    return f"Update status for '{title}': {result}"


@tool
def taskDelete(id: str):
    """
    Deletes a task using id 
    """
    with SessionLocal() as db:
        task_data = deleteTask(id=id)
        result = delete_task(data=task_data, db=db)
        
    return f"Delete status for '{id}': {result}"


tools = [newTask, TaskUpdate, readTasks, taskDelete]
