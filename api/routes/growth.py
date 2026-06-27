from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from api.deps.db import get_db
from api.deps.auth import get_current_user

from services.growth_service import (
    get_questions_by_category,
    create_answer,
    get_user_answers,

    generate_ai_questions,
    save_logical_answer,
    analyze_answers
)

from schemas.growth import (
    AnswerCreate,
    QuestionResponse,
    AnswerResponse
)

from schemas.thinking.logical import (
    LogicalQuestionRequest,
    LogicalAnswerRequest,
    LogicalAnalyzeRequest
)

router = APIRouter(
    prefix="/growth",
    tags=["Growth"]
)


# ===================================================
# Growth
# ===================================================

@router.get(
    "/questions/{category}",
    response_model=list[QuestionResponse],
    status_code=status.HTTP_200_OK
)
def get_questions(
    category: str,
    db: Session = Depends(get_db)
):
    return get_questions_by_category(
        db,
        category
    )


@router.post(
    "/answers",
    response_model=AnswerResponse,
    status_code=status.HTTP_201_CREATED
)
def submit_answer(
    data: AnswerCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return create_answer(
        db=db,
        user_id=current_user["id"],
        question_id=data.question_id,
        answer=data.answer
    )


@router.get(
    "/my-answers",
    response_model=list[AnswerResponse],
    status_code=status.HTTP_200_OK
)
def my_answers(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return get_user_answers(
        db,
        current_user["id"]
    )


# ===================================================
# Logical Thinking AI
# ===================================================

@router.post(
    "/logical/questions",
    status_code=status.HTTP_200_OK
)
def logical_questions(
    data: LogicalQuestionRequest
):

    return {

        "success": True,

        "data": generate_ai_questions(
            data.scenario
        )

    }


@router.post(
    "/logical/answer",
    status_code=status.HTTP_201_CREATED
)
def logical_answer(
    data: LogicalAnswerRequest,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):

    return save_logical_answer(

        db=db,

        user_id=current_user["id"],

        question_id=data.question_id,

        step=data.step,

        ai_question=data.ai_question,

        answer=data.answer

    )


@router.post(
    "/logical/analyze",
    status_code=status.HTTP_200_OK
)
def logical_analyze(
    data: LogicalAnalyzeRequest,
    db: Session = Depends(get_db)
):

    return {

        "success": True,

        "data": analyze_answers(
            db,
            data.question_id
        )

    }