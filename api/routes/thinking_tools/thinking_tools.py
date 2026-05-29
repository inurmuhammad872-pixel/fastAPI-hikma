from fastapi import APIRouter

from schemas.thinking_tools.thinking_tools import SWOTRequest
from schemas.thinking_tools.five_why import FiveWhyRequest
from schemas.thinking_tools.pareto import ParetoRequest
from schemas.thinking_tools.decision_matrix import DecisionMatrixRequest
from schemas.thinking_tools.pdsa import PDSARequest
from schemas.thinking_tools.disc import DISCRequest
from schemas.thinking_tools.skill_map import SkillMapRequest

from services.ai.swot_service import analyze_swot
from services.ai.five_why_service import analyze_five_why
from services.ai.pareto_service import analyze_pareto
from services.ai.decision_matrix_service import analyze_decision_matrix
from services.ai.pdsa_service import analyze_pdsa

from services.disc_service import analyze_disc
from services.skill_map_service import analyze_skill_map


router = APIRouter(
    prefix="/thinking-tools",
    tags=["Thinking Tools"]
)


@router.post("/swot")
async def swot_analysis(data: SWOTRequest):

    result = analyze_swot(data)

    return {
        "success": True,
        "data": result
    }


@router.post("/5why")
async def five_why_analysis(data: FiveWhyRequest):

    result = analyze_five_why(data)

    return {
        "success": True,
        "data": result
    }


@router.post("/pareto")
async def pareto_analysis(data: ParetoRequest):

    result = analyze_pareto(data)

    return {
        "success": True,
        "data": result
    }


@router.post("/decision-matrix")
async def decision_matrix_analysis(data: DecisionMatrixRequest):

    result = analyze_decision_matrix(data)

    return {
        "success": True,
        "data": result
    }


@router.post("/pdsa")
async def pdsa_analysis(data: PDSARequest):

    result = analyze_pdsa(data)

    return {
        "success": True,
        "data": result
    }


@router.post("/disc")
async def disc_analysis(data: DISCRequest):

    result = analyze_disc(data)

    return {
        "success": True,
        "data": result
    }


@router.post("/skill-map")
async def skill_map_analysis(data: SkillMapRequest):

    result = analyze_skill_map(data)

    return {
        "success": True,
        "data": result
    }