from langchain.agents import create_agent
import os
import dotenv

dotenv.load_dotenv()

def get_weather(news: str) -> str: 
    """get the latest weather information"""

    return f"The latest weather information for birmingham UK."

system_prompt = """You are an expert weatherman"""

agent = create_agent(
    model= "openai:gpt-5.4",
    system_prompt=system_prompt,
    tools=[get_weather]
)

result = agent.invoke(
    {"messages": [{"role": "user", "content": "what's the weather in birmingham?"}]}
)
print(result["messages"][-1].content_blocks)
