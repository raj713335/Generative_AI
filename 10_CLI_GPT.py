from langchain.tools import ShellTool
from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from dotenv import load_dotenv
import os

shell_tool = ShellTool()
load_dotenv()

OpenAI_key = os.environ.get("OPEN_AI_KEY")

llm = ChatOpenAI(openai_api_key=OpenAI_key, temperature=0)

shell_tool.description = shell_tool.description + f"args {shell_tool.args}".replace(
    "{", "{{"
).replace("}", "}}")
agent = initialize_agent(
    [shell_tool], llm, agent=AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION, verbose=True
)

agent.run(
    "create a text file called empty and inside it, add code that trains a basic convolutional neural network for 4 epochs"
)
