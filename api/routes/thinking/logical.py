from fastapi import APIRouter

from schemas.thinking.logical import (
    LogicalAnswerRequest,
    LogicalQuestionRequest,
    LogicalAnalyzeRequest
)

from services.ai.logical_service import (
    generate_logical_questions,
    analyze_logical_answers
)

router = APIRouter(
    prefix="/thinking/logical",
    tags=["Thinking"]
)


@router.post("/answer")
def answer(data: LogicalAnswerRequest):

    return {
        "success": True,
        "data": {
            "message": "Answer saved.",
            "answer": data.answer
        }
    }


@router.post("/questions")
def questions(data: LogicalQuestionRequest):

    return {
        "success": True,
        "data": generate_logical_questions(
            data.scenario
        )
    }


@router.post("/analyze")
def analyze(data: LogicalAnalyzeRequest):

    return {
        "success": True,
        "data": analyze_logical_answers(
            data.scenario,
            data.answers
        )
    }