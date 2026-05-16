from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session


from db.database import get_db
from schemas.focus import FocusStartSchema, FocusSessionResponse
from services.focus_service import (
    create_focus_session,
    end_focus_session_service,
    get_focus_session_status_service,
    get_focus_history_service,
    get_active_focus_session_service, 
    cancel_focus_session_service
)


router = APIRouter(
    prefix="/focus",
    tags=["Focus Session"]
)

@router.post("/start")
def start_focus_session(
    data: FocusStartSchema,
    db: Session = Depends(get_db)
):

    session = create_focus_session(
        db,
        data.user_id,
        data.duration
    )

    return {
        "message": "Fokus boshlandi",
        "session_id": session.id
    }


@router.post("/end/{session_id}")
def end_focus_session(
    session_id: int,
    db: Session = Depends(get_db)
):

    session = end_focus_session_service(
        db,
        session_id
    )

    return {
        "message": "Fokus tugatildi",
        "session_id": session.id
    }



@router.get(
    "/status/{session_id}",
    response_model=FocusSessionResponse
)
def get_focus_session_status(
    session_id: int,
    db: Session = Depends(get_db)
):

    session = get_focus_session_status_service(
        db,
        session_id
    )

    return {
        "session_id": session.id,
        "user_id": session.user_id,
        "duration": session.duration,
        "started_at": session.started_at,
        "ended_at": session.ended_at,
        "status": session.status
    }

@router.get("/history/{user_id}")
def get_focus_history(
    user_id: int,
    db: Session = Depends(get_db)
):

    focus_sessions = get_focus_history_service(
        db,
        user_id
    )

    return [
        {
            "session_id": s.id,
            "duration": s.duration,
            "started_at": s.started_at,
            "ended_at": s.ended_at,
            "status": s.status
        }
        for s in focus_sessions
    ]

@router.get("/active/{user_id}")
def get_active_focus_session(
    user_id: int,
    db: Session = Depends(get_db)
):

    active_session = get_active_focus_session_service(
        db,
        user_id
    )

    if not active_session:
        return {
            "active": False
        }

    return {
        "active": True,
        "session_id": active_session.id,
        "duration": active_session.duration,
        "started_at": active_session.started_at,
        "status": active_session.status
    }

@router.post("/cancel/{session_id}")
def cancel_focus_session(
    session_id: int,
    db: Session = Depends(get_db)
):

    session = cancel_focus_session_service(
        db,
        session_id
    )

    return {
        "message": "Sessiya bekor qilindi",
        "session_id": session.id
    }

