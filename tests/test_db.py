from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.main import app


#adding testing db in sqlite
DATABASE_URL = "sqlite:///test.db"

#add sttatic pool and connect args
engine = create_engine(
    DATABASE_URL, 
    connect_args={
        "check_same_thread": False, 
    },
    poolclass = StaticPool
)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


client = TestClient(app)

def overide_get_db(): 
    db = TestingSessionLocal()
    try: 
        yield db
    finally: 
        db.close

app.dependency_overrides[get_db] = override_get_db

