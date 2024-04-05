from langchain.chat_models import ChatOpenAI
from langchain.llms import OpenAI
from langchain.agents import load_tools, initialize_agent
from langchain.agents import AgentType

from dotenv import load_dotenv
import os

load_dotenv()

OpenAI_key = os.environ.get("OPEN_AI_KEY")

llm = ChatOpenAI(openai_api_key=OpenAI_key, temperature=0.5)
math_llm = OpenAI(openai_api_key=OpenAI_key, temperature=0.5)
tools = load_tools(
    ["human", "llm-math"],
    llm=math_llm,
)

agent_chain = initialize_agent(
    tools,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
)

agent_chain.run("what is my math problem and its solution")

