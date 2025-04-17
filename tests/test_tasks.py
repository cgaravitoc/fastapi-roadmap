from fastapi.testclient import TestClient
from main import app


client = TestClient(app)

def test_health_check():
    response = client.get("/")
    assert response.status_code == 200 or response.status_code == 404  # según si tienes un endpoint raíz

def get_token(): 
    response = client.post(
        "/login", 
        data={
            "username": "admin", 
            "password": "admin123"
        }
    )
    assert response.status_code == 200
    return response.json()["access_token"]


def test_login():
    token = get_token()
    assert token.startswith("ey")

# Paso 4: Crear tarea autenticado
def test_create_task_authenticated():
    token = get_token()
    headers = {"Authorization": f"Bearer {token}"}
    response = client.post("/tasks/", json={
        "title": "Tarea de prueba",
        "description": "Creada desde test",
        "completed": False
    }, headers=headers)

    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Tarea de prueba"
    assert data["completed"] is False

# Paso 5: Obtener tarea por ID
def test_get_task_by_id():
    token = get_token()
    headers = {"Authorization": f"Bearer {token}"}

    # Crear tarea
    create_response = client.post("/tasks/", json={
        "title": "Tarea con ID",
        "description": "Buscar por ID",
        "completed": False
    }, headers=headers)
    task_id = create_response.json()["id"]

    # Obtener tarea
    get_response = client.get(f"/tasks/{task_id}", headers=headers)
    assert get_response.status_code == 200
    assert get_response.json()["title"] == "Tarea con ID"

# Paso 6: Eliminar tarea
def test_delete_task():
    token = get_token()
    headers = {"Authorization": f"Bearer {token}"}

    # Crear tarea
    create_response = client.post("/tasks/", json={
        "title": "Tarea a eliminar",
        "description": "",
        "completed": False
    }, headers=headers)
    task_id = create_response.json()["id"]

    # Eliminarla
    delete_response = client.delete(f"/tasks/{task_id}", headers=headers)
    assert delete_response.status_code == 200
    assert delete_response.json()["message"] == "Tarea eliminada correctamente"