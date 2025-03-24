from langchain_openai import ChatOpenAI
from browser_use import Agent, Browser, BrowserConfig
from dotenv import load_dotenv
load_dotenv()

import asyncio

llm = ChatOpenAI(model="gpt-4o")
 

async def main():
    agent = Agent(
        task="搜索有关AI的最新新闻",
        llm=llm
    )
    result = await agent.run()
    print(result)

asyncio.run(main())