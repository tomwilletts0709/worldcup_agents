from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_check_returns_ok(): 
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_health_check_database_healthy(monkeypatch): 
    async def mock_db_health_check():
        return True

    monkeypatch.setattr(
        "app.core.database.check_database_health", mock_db_health_check
    )

    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "ok"
    assert response.json()["database"] == "healthy"


def test_health_check_database_unhealthy(monkeypatch): 
    async def mock_db_health_check():
        return False

    monkeypatch.setattr(
        "app.core.database.check_database_health", mock_db_health_check
    )

    response = client.get("/health")

    assert response.status_code == 503
    assert response.json()["status"] == "error"
    assert response.json()["database"] == "unhealthy"