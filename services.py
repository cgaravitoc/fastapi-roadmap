from models import Task
from fastapi import HTTPException

# Lista en memoria como almacenamiento temporal
tasks_db = []

def get_all_tasks():
    return tasks_db

def get_task_by_id(task_id: int):
    for task in tasks_db:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail="Tarea no encontrada")

def create_task(task: Task):
    if any(t.id == task.id for t in tasks_db):
        raise HTTPException(status_code=400, detail="ID ya existe.")
    tasks_db.append(task)
    return task

def update_task(task_id: int, updated_task: Task):
    for idx, task in enumerate(tasks_db):
        if task.id == task_id:
            tasks_db[idx] = updated_task
            return updated_task
    raise HTTPException(status_code=404, detail="Tarea no encontrada")

def delete_task(task_id: int):
    for idx, task in enumerate(tasks_db):
        if task.id == task_id:
            return tasks_db.pop(idx)
    raise HTTPException(status_code=404, detail="Tarea no encontrada")