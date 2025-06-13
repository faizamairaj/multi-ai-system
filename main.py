from agent import myAgent
import chainlit as cl
import asyncio

@cl.on_chat_start
async def on_chat_start():
    await cl.Message ( 
        content="Welcome! Ask anything about your project, and I will coordinate with specialists to assist you?"
        ).send()

    
@cl.on_message
async def main(message: cl.Message):
    user_input = message.content
    response = asyncio.run(myAgent(user_input))
    await cl.Message(
        content=f"{response}"
        ).send()
