import pytest 
from datetime import datetime


@pytest.fixture
def test_read_db(): 
    # Simulate a database connection and return a test database object
    class TestDB:
        def __init__(self):
            self.data = {"users": []}
        
        def add_user(self, user):
            self.data["users"].append(user)
    
    return TestDB()
