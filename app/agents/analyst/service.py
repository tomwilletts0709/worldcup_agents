from typing import List, Any

from app.agents.analyst.agent import analyst_agent
from app.agents.analyst.config import AnalystConfig
from app.agents.analyst.repository import AnalystRepository
from app.agents.analyst.models import AnalysisType, AnalysisStatus


class AnalystService: 
    def __init__(self, repository=AnalystRepository, analysis_status=AnalysisStatus, agent=analyst_agent, config=AnalystConfig(), tools=[get_user_memory, save_user_memory, get_player_stats, generate_report, tavily_search_tool]):
        self.agent = agent
        self.config = config
        self.tools = tools
        self.analysis_status = analysis_status
        self.repository = repository
    
    async def run_analysis(self, team_name: str, user_id: str) -> str: 
        """ This method will be called to analyse a team based on their latest statistics and generate a report. It will also save the user's preferences and memory for future interactions.
        for simplicity, we will just return a placeholder report here.
        """
        team_stats = get_team_stats(team_name)
        if team_stats is None:
            return f"No statistics found for team {team_name}."
        report = generate_team_report(team_name, team_stats)
        save_user_memory(user_id, {"last_analyzed_team": team_name, "report": report})
        return report
    
        agent_response = self.agent.run(
            input=f"Analyse the team {team_name} and generate a report based on the latest statistics. Save the user's preferences and memory for future interactions.",
            tools=self.tools,
            config=self.config.dict()
        )


    async def scout_opposition(self, team_name: str, player_name: str, user_id: str) -> Analysis: 
        report = Scout_Report(
            team_name=team_name,
            player_name=player_name,
            status=AnalysisStatus.PENDING
        )
        report = self.repository.create(report)
        if report is None:
            raise ValueError
        
        

#need to add ability to 
    