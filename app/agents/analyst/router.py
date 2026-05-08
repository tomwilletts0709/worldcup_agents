from typing import Any
from langchain.chat_models import ChatOpenAI
from langchain.agents import create_agent
from app.analyst.agent import analyst_agent
from app.analyst.config import AnalystConfig
from app.analyst.prompts import analyst_prompt  



@app.get("/analyse/player/{player_name}")
async def analyse_player(player_name: str, user_id: str) -> str:
    """Endpoint to analyse an individual player based on the latest statistics and generate a report. It will also save the user's preferences and memory for future interactions."""
    service = AnalystService()
    report = await service.analyse_player(player_name, user_id)
    return report

@app.get("/analyse/team/{team_name}")
async def analyse_team(team_name: str, user_id: str) -> str:
    """Endpoint to analyse a team based on their latest statistics and generate a report. It will also save the user's preferences and memory for future interactions."""
    service = AnalystService()
    report = await service.analyse_team(team_name, user_id)
    return report

@app.get("/analyse/topic/{topic}")
async def analyse_topic(topic: str, user_id: str) -> str:
    """Endpoint to analyse a specific topic related to football, such as a recent match, a tactical analysis, or a player comparison. It will also save the user's preferences and memory for future interactions."""
    service = AnalystService()
    report = await service.analyse_topic(topic, user_id)
    return report

@app.post("/analyse/custom")
async def analyse_custom(query: str, user_id: str) -> str:
    """Endpoint to allow users to ask custom analysis questions related to football. The agent will use its tools and knowledge to provide a comprehensive answer. It will also save the user's preferences and memory for future interactions."""
    service = AnalystService()
    response = await service.analyse_custom(query, user_id)
    return response