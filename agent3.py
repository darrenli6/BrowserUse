from pydantic import BaseModel
from typing import List  # 添加了缺失的导入
from langchain_openai import ChatOpenAI
from browser_use import Agent, Controller
import asyncio
# 使用Pydantic模型定义输出格式
class Post(BaseModel):
    post_title: str
    post_url: str
    num_comments: int
    hours_since_post: int


class Posts(BaseModel):
    posts: List[Post]


controller = Controller(output_model=Posts)


async def main():
    task = '前往hackernews的show hn页面并获取前5篇帖子'
    model = ChatOpenAI(model='gpt-4o')
    agent = Agent(task=task, llm=model, controller=controller)

    history = await agent.run()

    result = history.final_result()
    if result:
        parsed: Posts = Posts.model_validate_json(result)

        for post in parsed.posts:
            print('\n--------------------------------')
            print(f'标题:            {post.post_title}')
            print(f'网址:            {post.post_url}')
            print(f'评论数:          {post.num_comments}')
            print(f'发布后小时数:    {post.hours_since_post}')
    else:
        print('无结果')


if __name__ == '__main__':
    asyncio.run(main())