from typing import List, Any

from app.analyst.agent import analyst_agent
from app.analyst.config import AnalystConfig
from app.analyst.tools import (
    get_user_memory, 
    save_user_memory,
    get_player_stats,
    generate_report,
    tavily_search_tool
)
from app.analyst.prompts import analyst_prompt
from app.analyst.models import AnalysisType, AnalysisStatus
from app.analyst.prompts import analyst_prompt
from app.core.logging import logger

logger.info()



class AnalystService: 
    def __init__(self, analysis_status=AnalysisStatus, agent=analyst_agent, config=AnalystConfig(), tools=[get_user_memory, save_user_memory, get_player_stats, generate_report, tavily_search_tool]):
        self.agent = agent
        self.config = config
        self.tools = tools
        self.analysis_status = analysis_status

    async def analyse_player(self, player_name: str, user_id: str) -> str:
        """ This method will be called to analyse an individual player
        based on the latest statistics and generate a report. It will also save the user's preferences and memory for future interactions.
        """
        player_stats = get_player_stats(player_name)
        if player_stats is None: 
            return f"No statistics found for player {player_name}."
        report = generate_report(player_name, player_stats)
        save_user_memory(user_id, {"last_analyzed_player": player_name, "report": report})
        return report

        agent_response = self.agent.run(
            input=f"Analyse the player {player_name} and generate a report based on the latest statistics. Save the user's preferences and memory for future interactions.",
            tools=self.tools,
            config=self.config.dict()
        )
    
    
    async def analyse_team(self, team_name: str, user_id: str) -> str: 
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

    async def analyse_topic(self, topic: str) -> str: 
        """ This method will be called when the user wants to analyse a specific topic 
        of their choice about a team, a player, a match, a tactic and so on"""
        agent_response = self.agent.run(
            input
        )


#need to add ability to 
    