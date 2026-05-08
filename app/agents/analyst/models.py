from datetime import datetime
from enum import Enum
from typing import Optional

from sqlalchemy import DateTime
from sqlalchemy import Enum as SQLAlchemyEnum
from sqlalchemy import Float, Integer, JSON, String, Text, func
from sqlalchemy.ext.mutable import MutableList
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


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


def _enum_values(enum_cls: type[Enum]) -> list[str]:
    return [member.value for member in enum_cls]


class AnalystAgent(Base):
    __tablename__ = "analyst_agents"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)


class AnalystAgentInput(Base):
    __tablename__ = "analyst_agent_inputs"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    topic: Mapped[list[str]] = mapped_column(
        MutableList.as_mutable(JSON),
        default=list,
        nullable=False,
    )
    input: Mapped[str] = mapped_column(Text, nullable=False)
    fixture_id: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    session_id: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)


class Analysis(Base):
    __tablename__ = "analyses"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    topic: Mapped[list[str]] = mapped_column(
        MutableList.as_mutable(JSON),
        default=list,
        nullable=False,
    )
    input: Mapped[str] = mapped_column(Text, nullable=False)
    fixture_id: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    session_id: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    player_name: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    team_name: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    output: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    analysis_type: Mapped[Optional[AnalysisType]] = mapped_column(
        SQLAlchemyEnum(
            AnalysisType,
            values_callable=_enum_values,
            native_enum=False,
            length=32,
        ),
        nullable=True,
    )
    status: Mapped[AnalysisStatus] = mapped_column(
        SQLAlchemyEnum(
            AnalysisStatus,
            values_callable=_enum_values,
            native_enum=False,
            length=32,
        ),
        default=AnalysisStatus.PENDING,
        nullable=False,
    )
    confidence: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    sources: Mapped[Optional[list[str]]] = mapped_column(
        MutableList.as_mutable(JSON),
        nullable=True,
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )
