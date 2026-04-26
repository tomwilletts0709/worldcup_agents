from sqlmodel import SQLModel, Field, create_engine, session
from datetime import datetime
from typing import Optional, List, Any
from enum import Enum
from app.agents._common import AgentBase


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

class AnalystAgent(SQLModel, table=True, schema="analyst"):
    id: AgentBase = Field(default=None, primary_key=True)
    name: str
    description: str = Field(..., "This agent analyses data on players, matches, tactics to provide insight to the user:")

class AnalystAgentInput(SQLModel, table=True, schema="analyst"): 
    id: AgentBase = Field(default=None, primary_key=True)
    topic: List[str]
    input: str
    fixture_id: Optional[int]
    session_id: Optional[int]

class Analysis(SQLModel, table=True, schema="analyst"): 
    id: AgentBase = Field(default=None, primary_key=True)
    topic: List[str]
    input: str
    fixture_id: Optional[int] = Field(default = None, primary_key="fixture.id")
    session_id: Optional[int]
    output: Optional[str] = None
    analysis_type: Optional[AnalysisType] = None
    status: AnalysisStatus = AnalysisStatus.PENDING
    confidence: Optional[float] = None
    sources: Optional[List[str]] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


