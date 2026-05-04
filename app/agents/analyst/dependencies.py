from typing import Annotated

from fastapi import Depends 
from sqlalchemy.orm import Session

from app.agents.analyst.repository import AnalystRepository
from app.db import get_session


DbSession = Annotated[Session, Depends(get_session)]


def get_analyst_repository(db: DbSession) -> AnalystRepository:
    return AnalystRepository(db=db)


AnalystRepositoryDep = Annotated[
    AnalystRepository,
    Depends(get_analyst_repository),
]
