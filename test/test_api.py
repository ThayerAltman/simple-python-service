from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/health-check")
    assert response.status_code == 200

def test_api_invalid_path():
    response = client.get("/invalid_path")
    assert response.status_code == 404

def test_api_root():
    response = client.get("/")
    assert response.status_code == 200