from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_create_and_get_note():
    response = client.post("/notes/1?content=hello")
    assert response.status_code == 200
    response = client.get("/notes/1")
    assert response.json()["content"] == "hello"