#! pip install youtube_search

from langchain.tools import YouTubeSearchTool
from langchain.agents import initialize_agent, Tool
from langchain.agents import AgentType
from langchain.llms import OpenAI
from langchain import LLMMathChain, SerpAPIWrapper
from dotenv import load_dotenv
import os

load_dotenv()

OpenAI_key = os.environ.get("OPEN_AI_KEY")

tool = YouTubeSearchTool()

tools = [
    Tool(
        name="Search",
        func=tool.run,
        description="useful for when you need to give links to youtube videos. Remember to put https://youtube.com/ in front of every link to complete it",
    )
]

agent = initialize_agent(
    tools,
    OpenAI(openai_api_key=OpenAI_key, temperature=0),
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
)

agent.run('Whats a joe rogan video on an interesting topic')
