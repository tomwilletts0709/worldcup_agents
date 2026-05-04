from typing import Any
from langchain.tools import tool, ToolRuntime
from langgraph.store.memory import InMemoryStore
from pydantic import BaseModel, Field
from langchain_tavily import TavilySearch


@tool("access_user_memory", return_direct=True)
def get_user_memory(user_id: str, runtime: ToolRuntime) -> str: 
    """access and look up user memory"""
    store = runtime.store
    user_info = store.get(("users"), user_id)
    return str(user_info) if user_info else "No memory found for this user."

@tool 
def save_user_memory(user_id: str, user_info: dict[str, Any])
    """save userinfo"""
    store = runtime.store
    store.put(("users"), user_id, user_info)
    return "User memory saved successfully."

@tool("get_player_stats", return_direct=True)
def get_player_stats(player_name: str) -> dict: 
    """get the latest statistics for a given player, including goals scored, assists, and overall performance metrics."""
    return {
        "player_name": player_name,
        "goals_scored": 10,
        "assists": 5,
        "overall_performance": "Excellent"
    }

@tool("generate_report", return_direct=True)
def generate_report(player_name: str, stats: dict) -> str:
    """generate a detailed report based on the player's statistics, highlighting key performance indicators and trends."""
    report = f"Report for {player_name}:\n"
    report += f"Goals Scored: {stats['goals_scored']}\n"
    report += f"Assists: {stats['assists']}\n"
    report += f"Overall Performance: {stats['overall_performance']}\n"
    return report

tavily_search_tool = TavilySearch(
    max_results=5,
    topic="Football Analysis"
)

@tool("scout opposition", return_direct=True)
def scout_opposition(player_name: str, team_name: str, stats: dict) -> dict[str, Any]:
    scout_opposition_report = f"Report for {team_name}"
    scout_opposition_report +=

    return scout_opposition_report