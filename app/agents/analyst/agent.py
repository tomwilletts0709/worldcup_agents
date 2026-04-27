from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from langchain.agents.middlweare import (
    SummarizationMiddleware, 
    ModelCallLimitMiddlware, 
    ToolRetryMiddleware, 
    ModelFallbackMiddleware
)
from app.agents.analyst.tools import 
import os
import dotenv
from app.core.settings import settings
from app.agents.analyst.config import AnalystConfig
from app.agents.analyst.prompts import analyst_prompt
from app.agents.analyst.tools import get_user_memory, save_user_memory, get_player_stats, generate_report, tavily_search_tool



model = ChatOpenAI(ß
    model= "openai:gpt-5.4",
    temperature=AnalystConfig.temprature,
    max_tokens=AnalystConfig.max_tokens,

)

analyst_agent = create_agent(
    model= model.model,
    system_prompt=analyst_prompt,
    tools=[get_user_memory, save_user_memory, get_player_stats, generate_report, tavily_search_tool
    ],

)

