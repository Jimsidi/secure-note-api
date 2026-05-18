from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_create_note():
    response = client.post("/notes/1?content=hello")
    assert response.status_code == 200
    assert response.json()["id"] == "1"
    assert response.json()["content"] == "hello"


def test_get_existing_note():
    client.post("/notes/2?content=devsecops")
    response = client.get("/notes/2")
    assert response.status_code == 200
    assert response.json()["content"] == "devsecops"


def test_get_nonexistent_note():
    response = client.get("/notes/999")
    assert response.status_code == 200
    assert response.json()["error"] == "Note not found"