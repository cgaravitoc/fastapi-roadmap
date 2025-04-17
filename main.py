
from fastapi import FastAPI, Depends
from models import Task
import services
from fastapi.security import OAuth2PasswordRequestForm
from auth import authenticate_user, create_access_token, get_current_user
from datetime import timedelta
from fastapi import HTTPException
from database import Base, engine
from models import Task as DBTask
from sqlalchemy.orm import Session
from database import SessionLocal
from schemas import TaskCreate, Task


Base.metadata.create_all(bind=engine)  # Crear las tablas en la base de datos


app = FastAPI()


def get_db(): 
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user: 
        raise HTTPException(status_code=400, detail="Credenciales incorrectas")
    
    access_token = create_access_token(
        data={"sub": user["username"]}, 
        expires_delta=timedelta(minutes=30)
    )
    return {"access_token": access_token, "token_type": "bearer"}
    

@app.post("/tasks/", response_model=Task)
def create_task(task: TaskCreate, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    db_task = DBTask(**task.dict())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task


@app.get("/tasks/", response_model=list[Task])
def read_tasks(db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    return db.query(DBTask).all()


@app.get("/tasks/{task_id}", response_model=Task)
def read_task(task_id: int, db: Session = Depends(get_db), current_user= Depends(get_current_user)):
    task = db.query(DBTask).filter(DBTask.id == task_id).first()
    if not task: 
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return task 


@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, task_update: TaskCreate, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    task = db.query(DBTask).filter(DBTask.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    for key, value in task_update.dict().items():
        setattr(task, key, value)
    db.commit()
    db.refresh(task)
    return task


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    task = db.query(DBTask).filter(DBTask.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    db.delete(task)
    db.commit()
    return {"message": "Tarea eliminada correctamente"}

