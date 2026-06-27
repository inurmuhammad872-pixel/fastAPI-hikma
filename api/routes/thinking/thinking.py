from fastapi import APIRouter

from schemas.thinking.logical import (
    LogicalQuestionRequest,
    LogicalAnalyzeRequest
)

from services.ai.logical_thinking_service import (
    generate_logical_questions,
    analyze_logical_answers
)

from schemas.thinking.creative import CreativeThinkingRequest
from schemas.thinking.cause_effect import CauseEffectRequest
from schemas.thinking.questioning import QuestioningRequest
from schemas.thinking.conclusion import ConclusionRequest

from services.ai.creative_thinking_service import evaluate_creative
from services.ai.cause_effect_service import evaluate_cause_effect
from services.ai.questioning_service import evaluate_questioning
from services.ai.conclusion_service import evaluate_conclusion

router = APIRouter(
    prefix="/thinking",
    tags=["Thinking"]
)


@router.post("/logical/questions")
async def logical_questions(data: LogicalQuestionRequest):

    result = generate_logical_questions(
        data.scenario
    )

    return {
        "success": True,
        "data": result
    }


@router.post("/logical/analyze")
async def logical_analyze(data: LogicalAnalyzeRequest):

    answers_text = "\n".join(
        [
            f"Question: {item.question}\nAnswer: {item.answer}"
            for item in data.answers
        ]
    )

    result = analyze_logical_answers(
        scenario=data.scenario,
        answers=answers_text
    )

    return {
        "success": True,
        "data": result
    }


@router.post("/creative")
async def creative_thinking(data: CreativeThinkingRequest):

    result = evaluate_creative(
        question=data.question,
        answer=data.answer
    )

    return {
        "success": True,
        "data": result
    }


@router.post("/cause-effect")
async def cause_effect(data: CauseEffectRequest):

    result = evaluate_cause_effect(
        question=data.question,
        answer=data.answer
    )

    return {
        "success": True,
        "data": result
    }


@router.post("/questioning")
async def questioning(data: QuestioningRequest):

    result = evaluate_questioning(
        question=data.question,
        answer=data.answer
    )

    return {
        "success": True,
        "data": result
    }


@router.post("/conclusion")
async def conclusion(data: ConclusionRequest):

    result = evaluate_conclusion(
        question=data.question,
        answer=data.answer
    )

    return {
        "success": True,
        "data": result
    }