from typing import Any
from app.agents.analyst.agent import run_team_analysis
from app.agents.analyst.repository import AnalystRepository
from app.agents.analyst.schemas import Analysis, AnalysisType, AnalysisStatus
from app.agents.analyst.exceptions import (
    InvalidInputException,
    AnalysisFailedException,
)

class AnalystService: 
    def __init__(self, analyst_agent,):
        self.agent = agent
        self.config = config
        self.tools = tools
        self.analysis_status = analysis_status
        self.repository = repository
    
    async def run_analysis(self, team_name: str, user_id: str) -> Analysis: 
        """ This method will be called to analyse a team based on their latest statistics and generate a report. It will also save the user's preferences and memory for future interactions.
        for simplicity, we will just return a placeholder report here.
        """
        if not team_name: 
            raise InvalidInputExecption(f"team is required to run an analysis.")
        
        analysis = Analysis(
            topic=["team_analysis", team_name],
            input=f"Analyse {team_name}"
            team_name=team_name,
            analysis_type=AnalysisType.STATS,
            status=AnalysisStatus.PENDING,
        )
        
        analysis = self.repository.create(analysis)


        try:
            analysis.status = AnalysisStatus.RUNNING
            analysis = self.repository.update(analysis)

            report = await run_team_analysis(
                team_name=team_name,
                user_id=user_id
            )

            analysis.output = report 
            analysis.stats = AnalysisStatus.COMPLETED

            
            
    async def scout_opposition(self, team_name: str, player_name: str, user_id: str, opposition_team: str) -> Analysis: 
        report = Scout_Report(
            team_name=team_name,
            player_name=player_name,
            opposition_name = opposition_team
            analysis_type= AnalysisType.NEXT_OPPOSITION
            status=AnalysisStatus.PENDING
        )

        report = self.repository.create(analysis)
        
        try: 
            self.analysis_status = AnalysisStatus.RUNNING
            analysis = self.repository.update(analysis)

            report = await run_opposition_analysis(
                user_id=user_id
                team_name=team_name,
                opposition_team=opposition_team
            )

            analysis.output = report 
            analysis.stats = AnalysisStatus.COMPLETED
        

#need to add ability to 
    