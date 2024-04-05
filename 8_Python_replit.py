from langchain.agents.agent_toolkits import create_python_agent
from langchain.tools.python.tool import PythonREPLTool
from langchain.python import PythonREPL
from langchain.llms.openai import OpenAI
from langchain.agents.agent_types import AgentType
from langchain.chat_models import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

OpenAI_key = os.environ.get("OPEN_AI_KEY")


agent_executor = create_python_agent(
    llm=OpenAI(openai_api_key=OpenAI_key, temperature=0.5, max_tokens=2000),
    tool=PythonREPLTool(),
    verbose=True,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
)

agent_executor.run("What is the 10th fibonacci number?")

