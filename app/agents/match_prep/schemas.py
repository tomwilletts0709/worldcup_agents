from pydantic import BaseModel, Field
from typing import Optional, Annotated, Any, List, TypedDict
from datetime import datetime
from enum import Enim


class AnalysisType(str, Enum): 
    FORM = "form"
    STATS = "stats"
    TACTICS = "tactics"
    PLAYERS = "player"
    HEAD_TO_HEAD = "head_to_head"
    NEXT_OPPOSITION = "next_opposition"


class AnalysisStatus(str, Enum): 
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"


class AnalystAgent(BaseModel):
    id: int 
    name: str
    description: str = Field(..., "This agent analyses data on players, matches, tactics to provide insight to the users")

class AgentInput(BaseModel): 
    id: int
    topic: list(str)
    input: str
    fixture_id: Optional[int]
    session_id: Optional[int]

class AgentOutput(BaseModel):
    id: int
    topic: list[str]    
    output: str
    analysis_type: AnalysisType
    status: AnalysisStatus
    Confidence: Optional[float] = None
    sources: list[str] = None
    created_at: datetime = Field(default_factory=datetime.utc)
    updated_at: datetime = Field(default_factor=datetime.utc)
    

