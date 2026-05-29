from openai import OpenAI
from dotenv import load_dotenv
import os
from services.ai.base_ai_service import ask_ai
from schemas.thinking_tools.thinking_tools import SWOTRequest

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def analyze_swot(data: SWOTRequest):

    prompt = f"""
    Topic: {data.topic}

    Strengths:
    {", ".join(data.strengths)}

    Weaknesses:
    {", ".join(data.weaknesses)}

    Opportunities:
    {", ".join(data.opportunities)}

    Threats:
    {", ".join(data.threats)}
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "system",
                "content": "You are a SWOT analysis assistant."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content