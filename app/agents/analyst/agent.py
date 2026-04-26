from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from langchain.agents.middlweare import (
    SummarizationMiddleware, 
    ModelCallLimitMiddlware, 
    ToolRetryMiddleware, 
    ModelFallbackMiddleware
)
import os
import dotenv
from app.core.settings import settings
from app.agents.analyst.config import AnalystConfig
from app.agents.analyst.prompts import analyst_propmt


model = ChatOpenAI(
    model= "openai:gpt-5.4",
    temperature=AnalystConfig.temprature,
    max_tokens=AnalystConfig.max_tokens,

)

analyst_agent = ChatOpenAI(
    model= "openai:gpt-5.4",
    system_prompt=system_prompt,
    tools=[get_weather]
)

