from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_sum_success():
    response = client.get("/sum?a=2&b=3")
    assert response.status_code == 200
    assert response.json() == {"result": 5}


def test_sum_invalid():
    response = client.get("/sum?a=2&b=abc")
    assert response.status_code == 422