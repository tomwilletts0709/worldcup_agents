from pydantic import BaseModel

class user(BaseModel): 
    name: str
    age: int
    email: str

class Agent(BaseModel): 
    name:str
    description: str

class AgentResponse(BaseModel): 
    response: str

