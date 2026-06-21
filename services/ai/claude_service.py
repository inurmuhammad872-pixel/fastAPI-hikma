import os

from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

client = Anthropic(
    api_key=os.getenv("CLAUDE_API_KEY")
)


def ask_claude(
    system_prompt: str,
    user_prompt: str
):

    response = client.messages.create(
        model="claude-sonnet-4-5",

        max_tokens=1000,

        system=system_prompt,

        messages=[
            {
                "role": "user",
                "content": user_prompt
            }
        ]
    )

    return response.content[0].text