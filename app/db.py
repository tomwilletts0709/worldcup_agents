from sqlmodel import Field, Session, SQLModel, create_engine
import psycopg2

DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/postgres"

def create_database(database, name, user, password, host, port):
    conn = psycopg2.connect(
        dbname="postgres",
        user=user,
        password=password,
        host=host,
        port=port
    )
    conn.autocommit = True
    cursor = conn.cursor()
    cursor.execute(f"CREATE DATABASE {database}")
    cursor.close()
    conn.close()

engine = create_engine(DATABASE_URL)

def init_db():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session



