# Testing the run Database 
from database.crud import create_task, read_tasks
from database.database_setup import SessionLocal
from database.schemas import TaskCreate

# Test 1 : Creation of new task 
mock_data = TaskCreate(title="New Task", description="Testing description")


# result = create_task(data=mock_data, db=db_dependency)
def readTasks():
    """
        Reads all the tasks from the database. 
        Returns data formatted strictly as: - Title: Description (Completed: True/False)
        """
    with SessionLocal() as db:
        tasks = read_tasks(db=db)
        
    # Format database models as simple strings for the LLM to read cleanly
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

result =  readTasks()
print(result)
