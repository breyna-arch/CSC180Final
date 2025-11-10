import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    FLOWCHART_AGENT_MODEL_SPEC = os.getenv('FLOWCHART_AGENT_MODEL_SPEC')