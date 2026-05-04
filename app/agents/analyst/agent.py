from typing import Any
from langchain.agents import create_agent, AgentSate
from langchain_openai import ChatOpenAI
from langchain.messages import AIMessage, AnyMessage
from langgraph.checkpoint.memory import InMemorySaver
from langchain.agents.middleware import (
    SummarizationMiddleware, 
    ModelCallLimitMiddlware, 
    ToolRetryMiddleware, 
    ModelFallbackMiddleware
)
from app.agents.analyst.tools import 
from app.core.settings import settings
from app.agents.analyst.config import AnalystConfig
from app.agents.analyst.prompts import analyst_prompt
from app.agents.analyst.tools import get_user_memory, save_user_memory, get_player_stats, generate_report, tavily_search_tool



class CustomAgentState(AgentState):
    user_id = int
    preferences: dict


model = ChatOpenAI(
    model= "openai:gpt-5.4",
    temperature=AnalystConfig.temprature,
    max_tokens=AnalystConfig.max_tokens,
    streaming=True

)

sub_agent = create_agent(
    model=model,
    tools = [tool]
)


analyst_agent = create_agent(
    model= model.model,
    system_prompt=analyst_prompt,
    tools=[get_user_memory, save_user_memory, get_player_stats, generate_report, tavily_search_tool],
    middleware=[
        SummarizationMiddleware(
            model="gpt-5.4-mini",
            trigger=("tokens", 4000),
            keep=("messages", 20)
        ),
        ModelCallLimitMiddlware(
            thread_limit=10,
            run_limit=5,
            exit_behavior="end"
        ),
        ModelFallbackMiddleware(
            "gpt-5.4-mini",
        ),

    ]

)

async def run_team_analysis(team_name: str, user_id: str) -> str:
    result = await analyst_agent.ainvoke({
        "messages": [
            {
                "role": "user",
                "content": (
                    f"Analyse the football team {team_name}. "
                    f"Use current form, statistics, key players, tactical strengths, "
                    f"weaknesses, and give a useful report. "
                    f"The user id is {user_id}, so use or save memory if helpful."
                ),
            }
        ]
    })

    return result["messages"][-1].content


async def scout_opposition_analysis(team_name: str, oppenent_name: str, user_id: str) -> str:
    result = await analyst_agent.ainvoke({
        "messages": [
            {
                "role": "user",
                "content": (
                    f"Analyse the opposition, {team_name}. "
                    f"Use current form, statistics, key players, tactical strengths, "
                    f"weaknesses, and give a useful report. "
                    f"The user id is {user_id}, so use or save memory if helpful."
                ),
            }
        ]
    })

    return result["messages"][-1].content


def _render_message_chunk(token: AIMessageChunk) -> None: 
    if token.text: 
        print(token.text, end='|')
    if token.tool_call_chunks: 
        print(token.tool_call_chunks)

def _render_completed_message(message: AnyMessage) -> None: 
    if isinstance(message, AIMessage) and message.tool_calls:
        print(f"Tool calls: {message_calls}")
    if isinstance(message, ToolMessage): 
        print(f"Tool response: {message.content_blocks}")

current_agent = None
for chunk in agent.stream(
    {"messages": [input_message]},
    stream_mode=["messages", "updates"],
    subgraphs=True,
    version="v2"

):
    if chunk["type"] == "messages": 
        token, metadata = chunk["data"]
        if agent_name := metadata.get(""):
            if agent_name != current_agent:
                print(f"{agent_name}")
                current_agent = agent_name
        if isinstance(token, AIMessage): 
            _render_message_chunk(token)
    elif chunk["type"] == "updates": 
        for source, update in chunk["data"].items(): 
            if source in ("model", "tools"):
                _render_completed_message(update["messages"][-1])
