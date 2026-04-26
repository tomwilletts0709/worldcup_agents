from models import User
from app.db import db, 



class UserRepository: 
    def __init__(self, db: db): 
        self.db = db

    def create_user(self, user: UserCreate) -> User: 
        db_create_user = User.model_validate(
            user_create, 
            update = {"hashed_password": self.hash_password(user_create.password)}
        )
        self.db.add(user)
        self.db.commit() 
        self.db.refresh(user)
        return user
    
    def update_user(self, user_id: int, user: UserUpdate) -> User: 
        db_user = self.db