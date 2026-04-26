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



model = ChatOpenAI(
    model= "openai:gpt-5.4",
    temperature=AnalystConfig.temprature,
    max_tokens=AnalystConfig.max_tokens,

)

analyst_agent = create_agent(
    model= model.model,
    system_prompt=analyst_prompt,

)

