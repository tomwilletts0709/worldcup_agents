from sqlalchemy import integer, mapped_column, String
from sqlalchemy.orm import DeclarativeBase
from .app.db import Base
from uuid import UUID
from datetime import datetime, timezone, timedelta



class User(Base):
    __tablename__ = "users"

    id: int = mapped_column(integer, primary_key=True)
    name: str = mapped_column(String(50))
    created_at: datetime = mapped_column(default=datetime.utcnow)
    updated_at: datetime = mapped_column(default=datetime.utcnow, onupdate=datetime.utcnow)



class Agent_Response(Base):
    __tablename__ = "agent_responses"

    id: int = mapped_column(integer, primary_key=True)
    response: str = mapped_column(String(500))
    created_at: datetime = mapped_column(default=datetime.utcnow)
    updated_at: datetime = mapped_column(default=datetime.utcnow, onupdate=datetime.utcnow)

class Agent_Memory(Base): 
    __tablename__ = "agent_memory"

    id: int = mapped_column(integer, primary_key=True)
    memory: str = mapped_column(String(500))
    created_at: datetime = mapped_column(default=datetime.utcnow)
    updated_at: datetime = mapped_column(default=datetime.utcnow, onupdate=datetime.utcnow)


    