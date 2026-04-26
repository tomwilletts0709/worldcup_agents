from sqlmodel import SQLModel, Field
from datetime import datetime, timedelta


class User(SQLModel, table=True): 
    user_id: int = Field(default = None, primary_key=True)
    username: str = Field(..., unique=True, min_length=3, max_length=50)
    email: str = Field(..., unique=True, regex=r'^\S+@\S+\.\S+$')
    hashed_password: str = Field(..., min_length=8)
    is_active: bool = Field(default=True)
    is_superuser: bool = Field(default=False)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow, onupdate=datetime.utcnow)


class CreateUser(SQLModel): 
    username: str = Field(..., min_length=3, max_length=50)
    email: str = Field(..., regex=r'^\S+@\S+\.\S+$')
    password: str = Field(..., min_length=8)


class UpdateUser(SQLModel): 
    username: str = Field(None, min_length=3, max_length=50)
    email: str = Field(None, regex=r'^\S+@\S+\.\S+$')
    password: str = Field(None, min_length=8)
    is_active: bool = None
    is_superuser: bool = None


    