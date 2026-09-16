from langchain_core.tools import tool
from database.crud import create_task, delete_task, update_task, read_tasks
from database.schemas import TaskCreate, deleteTask, updateTask
# Import your synchronous SessionLocal factory
from database.database_setup import SessionLocal 

@tool
async def newTask(title: str, description: str):
    """
    Add a new Task
    """
    # Open a clean synchronous database connection session
    with SessionLocal() as db:
        newTask_data = TaskCreate(title=title, description=description)
        result = create_task(data=newTask_data, db=db)
    
    return f"Task '{title}' has been successfully created."


@tool 
async def readTasks():
    """
        Reads all the tasks from the database. 
        Returns data formatted strictly as: - Title: Description (Completed: True/False)
        """
    with SessionLocal() as db:
        tasks = read_tasks(db=db)
        
    # Format database models as simple strings for the LLM to read cleanly
    task_strings = [f"- {t.title}: {t.description} (Completed: {t.completed})" for t in tasks]
    return "\n".join(task_strings) if task_strings else "No tasks found."





@tool
async def TaskUpdate(title: str, completed: bool):
    """
    Updates task as completed as True or False
    """
    with SessionLocal() as db:
        task_data = updateTask(title=title, completed=completed)
        result = update_task(data=task_data, db=db)
        
    return f"Update status for '{title}': {result}"


@tool
async def taskDelete(title: str):
    """
    Deletes a task
    """
    with SessionLocal() as db:
        task_data = deleteTask(title=title)
        result = delete_task(data=task_data, db=db)
        
    return f"Delete status for '{title}': {result}"


tools = [newTask, TaskUpdate, readTasks, taskDelete]
