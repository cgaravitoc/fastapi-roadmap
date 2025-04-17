from pydantic import BaseModel
from typing import Optional

class TaskBase(BaseModel): 
    title: str
    description: Optional[str] = None
    completed: Optional[bool] = False

class TaskCreate(TaskBase): 
    pass

class Task(TaskBase):
    id: int

    class Config:
        orm_mode = True  # Permite la conversión de modelos ORM a Pydantic