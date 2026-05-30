# api/routes/thinking.py

from fastapi import APIRouter

from schemas.thinking.logical import LogicalThinkingRequest
from schemas.thinking.creative import CreativeThinkingRequest
from schemas.thinking.cause_effect import CauseEffectRequest
from schemas.thinking.questioning import QuestioningRequest
from schemas.thinking.conclusion import ConclusionRequest

from services.ai.creative_thinking_service import evaluate_creative
from services.ai.cause_effect_service import evaluate_cause_effect
from services.ai.questioning_service import evaluate_questioning
from services.ai.conclusion_service import evaluate_conclusion
from services.ai.logical_thinking_service import evaluate_logical

router = APIRouter(
    prefix="/thinking",
    tags=["Thinking"]
)


@router.post("/logical")
async def logical_thinking(data: LogicalThinkingRequest):

    result = evaluate_logical(
        question=data.question,
        answer=data.answer
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
async def cause_effect_thinking(data: CauseEffectRequest):

    result = evaluate_cause_effect(
        question=data.question,
        answer=data.answer
    )

    return {
        "success": True,
        "data": result
    }


@router.post("/questioning")
async def questioning_thinking(data: QuestioningRequest):

    result = evaluate_questioning(
        question=data.question,
        answer=data.answer
    )

    return {
        "success": True,
        "data": result
    }


@router.post("/conclusion")
async def conclusion_thinking(data: ConclusionRequest):

    result = evaluate_conclusion(
        question=data.question,
        answer=data.answer
    )

    return {
        "success": True,
        "data": result
    }

# TODO:
# Critical Thinking AI Evaluation
# Will be implemented later