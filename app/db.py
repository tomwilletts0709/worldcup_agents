from collections.abc import Generator

import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker

DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/postgres"


class Base(DeclarativeBase):
    pass


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
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)


def init_db():
    import app.agents.analyst.models  # noqa: F401

    Base.metadata.create_all(bind=engine)


def get_session() -> Generator[Session, None, None]:
    with SessionLocal() as session:
        yield session
