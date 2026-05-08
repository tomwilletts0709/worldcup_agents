from app.analyst.router import (

)
from app.main import app
import pytest
from fastapi.testclient import TestClient


client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == "Server is running"


