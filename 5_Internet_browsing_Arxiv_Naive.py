from langchain.chat_models import ChatOpenAI
from langchain.agents import load_tools, initialize_agent, AgentType

# If the parser is throwing error out, remember to set temperature to a higher value!!!

# pip install arxiv

from dotenv import load_dotenv
import os

load_dotenv()

OpenAI_key = os.environ.get("OPEN_AI_KEY")

llm = ChatOpenAI(openai_api_key=OpenAI_key, temperature=0.3)
tools = load_tools(
    ["arxiv"]
)

agent_chain = initialize_agent(
    tools,
    llm,
    max_iterations=5,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
    handle_parsing_errors=True,  ### IMPORTANT
)

agent_chain.run(
    "what is Sonar?",
)
