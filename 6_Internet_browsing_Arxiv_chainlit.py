from langchain import OpenAI, LLMMathChain, SerpAPIWrapper
from langchain.agents import initialize_agent, Tool, AgentExecutor
from langchain.chat_models import ChatOpenAI
import os
import chainlit as cl
from langchain.chat_models import ChatOpenAI
from langchain.agents import load_tools, initialize_agent, AgentType
from dotenv import load_dotenv
import os

load_dotenv()

OpenAI_key = os.environ.get("OPEN_AI_KEY")


@cl.on_chat_start
def start():
    llm = ChatOpenAI(openai_api_key=OpenAI_key, temperature=0.5, streaming=True)
    tools = load_tools(
        ["arxiv"]
    )

    agent_chain = initialize_agent(
        tools,
        llm,
        max_iterations=10,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
        handle_parsing_errors=True,
    )

    cl.user_session.set("agent", agent_chain)


@cl.on_message
async def main(message):
    agent = cl.user_session.get("agent")  # type: AgentExecutor
    cb = cl.LangchainCallbackHandler(stream_final_answer=True)

    await cl.make_async(agent.run)(message, callbacks=[cb])
