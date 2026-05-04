from sqlalchemy import String, cast, select
from sqlalchemy.orm import Session

from app.agents.analyst.models import Analysis

class AnalystRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, analysis: Analysis) -> Analysis:
        if analysis.id is not None:
            raise ValueError("Cannot create an Analysis that already has an ID")
        self.db.add(analysis)
        self.db.flush()
        self.db.commit()
        self.db.refresh(analysis)
        return analysis

    def update(self, analysis: Analysis) -> Analysis:
        if analysis.id is None:
            raise ValueError("Cannot update an Analysis that has not been saved")
        self.db.add(analysis)
        self.db.flush()
        self.db.commit()
        self.db.refresh(analysis)
        return analysis

    def get_by_id(self, analysis_id: int) -> Analysis:
        if analysis_id is None:
            raise ValueError("analysis_id cannot be None")
        return self.db.get(Analysis, analysis_id)

    def get_by_topic(self, topic: str) -> list[Analysis]:
        statement = select(Analysis).where(cast(Analysis.topic, String).contains(topic))
        return list(self.db.scalars(statement).all())

    def get_by_player(self, player_name: str) -> list[Analysis]:
        if not player_name:
            raise ValueError("player_name cannot be empty")
        statement = select(Analysis).where(Analysis.player_name == player_name)
        return list(self.db.scalars(statement).all())

    def get_by_team(self, team_name: str) -> list[Analysis]:
        if not team_name:
            raise ValueError("team_name cannot be empty")
        statement = select(Analysis).where(Analysis.team_name == team_name)
        return list(self.db.scalars(statement).all())
    
    def delete(self, analysis_id: int) -> None: 
        result = self.db.get(Analysis, analysis_id)
        if result: 
            self.db.delete(result)
            self.db.commit()
