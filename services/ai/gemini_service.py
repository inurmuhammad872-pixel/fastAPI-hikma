import os

import google.generativeai as genai

from dotenv import load_dotenv

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)


def ask_gemini(
    system_prompt: str,
    user_prompt: str
):

    prompt = f"""
{system_prompt}

{user_prompt}
"""

    response = model.generate_content(
        prompt
    )

    return response.text