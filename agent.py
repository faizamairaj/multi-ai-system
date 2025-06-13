from dotenv import load_dotenv
from openai import AsyncOpenAI
from agents import Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI,set_tracing_disabled
import os

load_dotenv()
set_tracing_disabled(True)

provider = AsyncOpenAI(
api_key=os.getenv("GEMINI_API_KEY"),
base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

model = OpenAIChatCompletionsModel(
model="gemini-2.0-flash-exp",
openai_client=provider,
)

# Define the multi agents:
# Each agent has a specific role and instructions:

# web developer:
web_dev = Agent(
name="web_developer",
instructions="Design and implement a user-friendly web app for creating, editing, and managing daily tasks efficiently.",
model=model,
handoff_description="Please hand off to a web developer for implementation.",
)
# social media manager:
social_media = Agent(
name="Social Media Manager",
instructions="Develop and execute an engaging social media strategy to promote the web and mobile applications across key platforms.",
model=model,
handoff_description="Please hand off to a social media manager for implementation.",
)
# marketing specialist:
marketing = Agent(
name="Marketing Specialist",
instructions="Design a comprehensive marketing strategy to drive user acquisition and brand growth for the web and mobile applications.",
model=model,
handoff_description="Please hand off to a marketing specialist for implementation.",
)
# graphic designer:
graphic_designer = Agent(
name="Graphic Designer",
instructions="Create visually appealing and user-friendly UI designs for both web and mobile applications, ensuring brand consistency.",
model=model,
handoff_description="Please hand off to a graphic designer for implementation.",
)

async def myAgent(user_input):
    manager = Agent(
    name="Project Manager",
    instructions="Oversee the project, ensuring all tasks are completed on time and meet quality standards. Coordinate between web developer, social media manager, marketing specialist, and graphic designer.",
    model=model,
    handoff_description=[web_dev, social_media, marketing, graphic_designer],
    )

    response = await Runner.run(
    manager,
    input=user_input,
)
    return response.final_output

  