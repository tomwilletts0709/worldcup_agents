from sqlmodel import Session, select
from app.db import get_session
from app.agents.analyst.models import AnalystAgent, AnalystAgentInput, Analysis

class AnalystRepository: 
    def __init__(self, db: Session): 
        self.db = db

    def save(self, analysis: Analysis) -> AnalystAgent: 
        self.db.add(agent)
        self.db.commit()
        self.flush(analysis)
        self.db.refersh(analysis)
        return analysis
    
    def update(self, analysis: Analysis) -> AnalystAgent: 
        self.db.add(analysis)
        self.db.commit()
        self.db.flush(analysis)
        self.db.refresh(analysis)
        return 
    
    def get_by_topic(self, topic: str) -> list[Analysis]: 
        stat