from pydantic import BaseModel, Field
from datetime import datetime
from enum import Enum

class AgentRunningStatus(str, Enum):
    STOPPED = "stopped"
    RUNNING = "running"
    PAUSED = "paused"


class AgentBase(BaseModel): 
    id: int 
    name: str
    description: str
    status: AgentRunningStatus = AgentRunningStatus.STOPPED
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

