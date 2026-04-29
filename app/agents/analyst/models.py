from sqlmodel import SQLModel, Field
from sqlalchemy import Column, JSON
from datetime import datetime
from typing import Optional, List
from enum import Enum


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
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    description: str = Field(..., description="This agent analyses data on players, matches, tactics to provide insight to the user:")

class AnalystAgentInput(SQLModel, table=True, schema="analyst"):
    id: Optional[int] = Field(default=None, primary_key=True)
    topic: List[str] = Field(default=[], sa_column=Column(JSON))
    input: str
    fixture_id: Optional[int] = None
    session_id: Optional[int] = None

class Analysis(SQLModel, table=True, schema="analyst"):
    id: Optional[int] = Field(default=None, primary_key=True)
    topic: List[str] = Field(default=[], sa_column=Column(JSON))
    input: str
    fixture_id: Optional[int] = None
    session_id: Optional[int] = None
    player_name: Optional[str] = None
    team_name: Optional[str] = None
    output: Optional[str] = None
    analysis_type: Optional[AnalysisType] = None
    status: AnalysisStatus = AnalysisStatus.PENDING
    confidence: Optional[float] = None
    sources: Optional[List[str]] = Field(default=None, sa_column=Column(JSON))
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


