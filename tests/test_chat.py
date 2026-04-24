from langchain.core.laguage_models.fake_chat_models import GenericFakeChatMode

model = GenericFakeChatModel(
    message = iter([
        AIMessage(content="The weather today in New York is sunny with a high of 25 degrees Celsius and a low of 15 degrees Celsius.",
                  tools_calls=[ToolCall])
    ])

)