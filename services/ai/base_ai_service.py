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

    if provider == "claude":

        result = ask_claude(
            system_prompt=system_prompt,
            user_prompt=user_prompt
        )

        print("CLAUDE RESULT:", result)

        return result

    if provider == "gemini":

        result = ask_gemini(
            system_prompt=system_prompt,
            user_prompt=user_prompt
        )

        print("GEMINI RESULT:", result)

        return result

    response = client.chat.completions.create(

        model="gpt-4.1-mini",

        messages=[

            {
                "role": "system",
                "content": system_prompt
            },

            {
                "role": "user",
                "content": user_prompt
            }

        ],

        temperature=0.7
    )

    result = response.choices[0].message.content

    print("OPENAI RESULT:", result)

    return result