# schemas/thinking/logical.py

from pydantic import BaseModel


class LogicalThinkingRequest(BaseModel):
    question: str
    answer: str