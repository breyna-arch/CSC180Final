from main import initialize_everything
from retrieve_master_prompt import master_prompt
from agents import Agent, Runner, SQLiteSession
from mermaid_code_judge import codeJudge
import asyncio

async def insertPrompt(user_text):
    initialize_everything() # sets the OPENAI_API_KEY to environment variable, needed for agents SDK
    masterPrompt = master_prompt.main() # feeds the model spec into masterPrompt variable, for model to get its instructions

    flowchart_agent = Agent(
        name="Flowchart Agent",
        instructions=masterPrompt,
    )

    flowchart_session = SQLiteSession("conversation_1")

    result = await Runner.run(
        flowchart_agent,
        input=user_text,
        session=flowchart_session
    )

    return await codeJudge.main(result) # feed result into another LLM agent to judge code output