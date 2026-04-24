from pytest import TestClient
from app.main import app

client = TestClient(app)

@pytest.fixture
def test_read_root(): 
    assert client.get("/").json() == {"Hello": "World"}

