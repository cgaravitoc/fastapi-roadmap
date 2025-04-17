# 🧠 Roadmap para dominar los fundamentos de FastAPI

Una API moderna y segura para gestionar tareas (To-Do list), construida con **FastAPI**, **SQLAlchemy**, **JWT Auth** y conectada a un frontend React. Ideal para practicar arquitectura de APIs, autenticación y consumo desde frontend.

---

## 🚀 Tecnologías

- 🐍 **FastAPI** – Framework web moderno y asincrónico
- 🛢️ **SQLAlchemy** – ORM para persistencia de datos con SQLite
- 🔐 **JWT** – Autenticación segura con tokens
- ⚛️ **React** – Frontend SPA para consumir la API
- 🧪 **Pytest** – Pruebas unitarias para endpoints protegidos
- 🐳 **Docker** – (opcional) para empaquetar la app

---

## 📁 Estructura del proyecto

```
.
├── main.py              # App principal FastAPI
├── models.py            # ORM con SQLAlchemy
├── schemas.py           # Pydantic schemas
├── auth.py              # Lógica de autenticación JWT
├── database.py          # Configuración de conexión a base de datos
├── tests/
│   └── test_tasks.py    # Pruebas de endpoints
├── frontend/            # (Opcional) app React conectada
└── README.md
```

---

## ⚙️ Instalación y ejecución (backend)

1. Crea entorno virtual e instala dependencias:
```bash
python -m venv venv
source venv/bin/activate  # o venv\Scripts\activate en Windows
pip install -r requirements.txt
```

2. Ejecuta la API:
```bash
uvicorn main:app --reload
```

3. Documentación automática:
- Swagger: http://localhost:8000/docs
- Redoc: http://localhost:8000/redoc

---

## 🔐 Usuario de prueba

Puedes usar este usuario para login:

```
username: admin
password: admin123
```

---

## 🔧 Endpoints principales

| Método | Ruta         | Descripción                      |
|--------|--------------|----------------------------------|
| POST   | /login       | Autenticación y obtención del JWT|
| GET    | /tasks       | Obtener todas las tareas         |
| POST   | /tasks       | Crear nueva tarea                |
| GET    | /tasks/{id}  | Obtener tarea por ID             |
| PUT    | /tasks/{id}  | Actualizar tarea                 |
| DELETE | /tasks/{id}  | Eliminar tarea                   |

> Todos los endpoints están protegidos con JWT.

---

## 🧪 Ejecutar tests

```bash
pytest
```

---

## 📦 Docker (opcional)

```bash
docker build -t fastapi-todo .
docker run -d -p 8000:8000 fastapi-todo
```

---

## 📜 Licencia

Este proyecto está bajo la licencia MIT. Puedes usarlo, modificarlo y compartirlo libremente.

---