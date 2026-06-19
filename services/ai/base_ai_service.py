from openai import OpenAI
from dotenv import load_dotenv
import os

from services.ai.claude_service import ask_claude
from services.ai.gemini_service import ask_gemini
from services.ai.ai_router import get_provider

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def ask_ai(
    system_prompt: str,
    user_prompt: str,
    task_name: str
):

    print("NEW BASE AI IS WORKING")

    provider = get_provider(task_name)

    print("PROVIDER:", provider)