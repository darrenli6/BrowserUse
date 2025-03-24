from langchain_openai import ChatOpenAI
from browser_use import Agent, Browser, BrowserConfig
from dotenv import load_dotenv
load_dotenv()

import asyncio

llm = ChatOpenAI(model="gpt-4o")
 

async def main():
    agent = Agent(
        task="gpt-4o和DeepSeek-V3 比较一下价格",
        llm=llm
    )
    result = await agent.run()
    print(result)

asyncio.run(main())