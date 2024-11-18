import pytest
from app import app
from app.database import db


@pytest.fixture
def client():
    # Configure test database
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client

def test_create_task(client):
    response = client.post("/tasks", json={"title": "Test Task"})
    assert response.status_code == 201
    assert response.json["title"] == "Test Task"
    assert response.json["completed"] is False

def test_get_tasks(client):
    client.post("/tasks", json={"title": "Test Task"})
    response = client.get("/tasks")
    assert response.status_code == 200
    assert len(response.json) == 1
    assert response.json[0]["title"] == "Test Task"

def test_update_task(client):
    client.post("/tasks", json={"title": "Test Task"})
    response = client.put("/tasks/1", json={"title": "Updated Task", "completed": True})
    assert response.status_code == 200
    assert response.json["title"] == "Updated Task"
    assert response.json["completed"] is True

def test_delete_task(client):
    client.post("/tasks", json={"title": "Test Task"})
    response = client.delete("/tasks/1")
    assert response.status_code == 200
    assert response.json["message"] == "Task deleted"
