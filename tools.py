import os
from langchain_core.tools import tool
from database.crud import create_task,delete_task,update_task,read_tasks,db_dependency
from database.schemas import TaskCreate,deleteTask,updateTask

@tool
async def newTask(title:str,description:str):
    """
    Add a new Task
    """
    newTask = TaskCreate(title=title, description=description)
    result = await create_task(data=newTask, db=db_dependency)

    return result


@tool 
async def readTasks():
    """
    Reads all the tasks from database
    """

    tasks = await read_tasks(db_dependency)
    return tasks
    
    
@tool
async def TaskUpdate(title:str,completed:bool):
    """
    Updates task as completed as True or False
    """

    task = updateTask(title=title,completed=completed)
    result = await update_task(data=task,db=db_dependency)

    return result


@tool
async def taskDelete(title:str):
    """
    Deletes a task
    """

    task = deleteTask(title=title)
    result = await delete_task(data=task,db=db_dependency)

    return result


tools = [newTask,TaskUpdate,readTasks,taskDelete]
