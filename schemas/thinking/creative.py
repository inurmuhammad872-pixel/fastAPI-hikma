from pydantic import BaseModel


class CreativeThinkingRequest(BaseModel):
    question: str
    answer: str