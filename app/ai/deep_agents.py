from deepagents import create_deep_agents
from langchain.chat_models import init_chat_model
from ..core.settings import settings
from ..schemas import Agent

def get_weather(city: str) -> str:
    """get weather for a given city"""

    return f"The weather today in {city} is sunny with a high of 25 degrees Celsius and a low of 15 degrees Celsius."

system_prompt = """
You are an expert weather researcher.
You have access to a tool that can get the weather for a given city.
Use this tool to get the weather for any city that the user asks about."""




agent = create_deep_agent(
    model=init_chat_model(
    model="openai:gpt-5.4",
    system_prompt=system_prompt,
    tools=[get_weather],
    )
)

agent.invoke("what is the ")