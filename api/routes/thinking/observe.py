from fastapi import APIRouter

from schemas.thinking.observe import (

    ObserveQuestionRequest,

    ObserveAnalyzeRequest,

    ObserveConclusionRequest

)

from services.ai.observe_service import (

    generate_questions,

    analyze_answers,

    generate_feedback

)


router = APIRouter(

    prefix="/thinking/observe",

    tags=["Thinking"]
)


@router.post("/questions")

def questions(

    data: ObserveQuestionRequest

):

    return {

        "success": True,

        "data": generate_questions(

            data.scenario

        )
    }


@router.post("/analyze")

def analyze(

    data: ObserveAnalyzeRequest

):

    return {

        "success": True,

        "data": analyze_answers(

            data.scenario,

            data.answers

        )
    }


@router.post("/feedback")

def feedback(

    data: ObserveConclusionRequest

):

    return {

        "success": True,

        "data": generate_feedback(

            data.scenario,

            data.observe,

            data.reason,

            data.evidence,

            data.alternative,

            data.conclusion

        )
    }