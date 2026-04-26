from pydantic_settings import BaseSettings
from pydantic import Field




class AnalystConfig(BaseSettings):
    #llm
    model: str = Field(default="openai:gpt-5.4", description="The language model to use for the analyst agent")
    temprature: float = Field(default=0.7, description="The temperature to use for the analyst agent")
    max_tokens: int = Field(default=2048, description="The maximum number of tokens to generate for the analyst agent")
   
    #limiting 
    request_per_minute: int = Field(default=60, description="The number of requests per minute to allow for the analyst agent")
    request_per_day: int = Field(default=1000, description="The number of requests per day to allow for the analyst agent")

    #cache 
    cache_expire: int = Field(default=3600, description="The number of seconds to cache the analyst agent's responses")
    cache_seconds: int = Field(default=300, description="The number of seconds to cache the analyst agent's responses")

    #Agent behaviour
    max_retries: int = Field(default=3, description="The maximum number of retries for the analyst agent")
    verbose: bool = Field(default=False, description="Whether to enable verbose logging for the analyst agent")

    model_config = {
        "env_file": ".env",
        "env_file_encoding": "utf-8"
        "extra": "ignore"
    }

analyst_config = AnalystConfig()
    

