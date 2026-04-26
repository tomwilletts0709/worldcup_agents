from typing
from langchain.tools import tool, ToolRuntime
from langgraph.store.memory import InMemoryStore
from app.agents.analyst.models import 
from pydantic import BaseModel, Field
from langchain_tavily import TavilySearch

class 


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

tavily_search_tool = TavilySearch(
    max_results=5,
    topic="Football Analysis"
)