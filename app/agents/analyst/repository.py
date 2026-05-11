from sqlmodel import Session, select
from sqlalchemy import cast, String
from app.agents.analyst.schemas import AnalystAgent, AnalystAgentInput, Analysis

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


    def update(self, analysis_id: int) -> Analysis:
        statement = select(Analysis).where(Analysis.id == analysis_id)
        result = self.db.exec(statement).first()
        if result is None: 
            raise ValueError("No result found")

        self.db.commit()
        self.db.refresh(result)

        return result

    def get_by_topic(self, topic: str) -> list[Analysis]:
        statement = select(Analysis).where(cast(Analysis.topic, String).contains(topic))
        result = self.db.exec(statement).all()
        return result

    def get_by_player(self, player_name: str) -> list[Analysis]:
        if not player_name:
            raise ValueError("player_name cannot be empty")
        statement = select(Analysis).where(Analysis.player_name == player_name)
        result = self.db.exec(statement).all()
        return result

    def get_by_team(self, team_name: str) -> list[Analysis]:
        if not team_name:
            raise ValueError("team_name cannot be empty")
        statement = select(Analysis).where(Analysis.team_name == team_name)
        result = self.db.exec(statement).all()
        return result
    
    def delete(self, analysis_id: int) -> None: 
        statement = select(Analysis).where(Analysis.id == analysis_id)
        result = self.db.exec(statement).first()
        if result: 
            self.db.delete(result)
            self.db.commit()