from openai import AsyncOpenAI
from agents import Agent, OpenAIChatCompletionsModel, Runner, set_tracing_disabled
import os
from dotenv import load_dotenv
# set_tracing disbaled is used to secure our data fron sending to Open AI
set_tracing_disabled(disabled=True)


#Load API Key
load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")


# Create OpenAI-Compatible Client (for Gemini)
client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/", #this url comes from Google AI for developers (openAi compatibility)
)

"""Google Gemini exposes an OpenAI-compatible API if you hit the /openai endpoint.
So you can trick libraries into talking to Gemini like it’s OpenAI."""

agent = Agent(
    name="Assistant",
    instructions="You are an expert of agentic AI.",
    model=OpenAIChatCompletionsModel(model="gemini-2.0-flash", openai_client=client),
)

"""🔹 OpenAIChatCompletionsModel(...)
Tells the agent:

"Use the Gemini model with this client as if it were OpenAI"""

query = input("Enter the query or quit to exit: ")

while query != "quit":
    result = Runner.run_sync( #Calls the model with the user query

        # Internally does:

        # Add system prompt

        # Format messages

        # Run through OpenAIChatCompletionsModel

        # Collects the result
        agent,
        query,
    )
    print(result.final_output)
    query = input("Enter the query or quit to exit: ")