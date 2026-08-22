from fastapi.testclient import TestClient

from app import add, app

client = TestClient(app)


def test_add():
    assert add(2, 3) == 5


def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"result": 5}


def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
