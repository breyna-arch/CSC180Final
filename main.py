from config import Config
import os

def initialize_everything():
    os.environ["OPENAI_API_KEY"] = Config.OPENAI_API_KEY