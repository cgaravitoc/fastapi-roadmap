import requests

BASE_URL = "http://localhost:8000"

def login(username, password):
    data = {"username": username, "password": password}
    response = requests.post(f"{BASE_URL}/login", data=data)
    response.raise_for_status()
    return response.json()["access_token"]

def get_tasks(token):
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"{BASE_URL}/tasks", headers=headers)
    response.raise_for_status()
    return response.json()

if __name__ == "__main__":
    token = login("admin", "admin123")
    tasks = get_tasks(token)
    print(tasks)