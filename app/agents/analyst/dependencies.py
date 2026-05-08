from typing import Annotated
from fastapi import Depends
from sqlalchemy.orm import Session

from app.db import get_session
from app.agents.analyst.repository import AnalystRepository
from app.agents.analyst.service import AnalystService

Dbsession = Annotated[Session, Depends(get_session)]

def get_analyst_repository(db: Dbsession) -> AnalystRepository:
    return AnalystRepository(db=db)

AnalystRepositoryDep = Annotated[
    AnalystRepository,
    Depends(get_analyst_repository)
]