from fastapi import HTTPException
from datetime import datetime

from db.models.focus_session import FocusSession


def create_focus_session(db, user_id, duration):

    existing_session = db.query(FocusSession).filter(
        FocusSession.user_id == user_id,
        FocusSession.status == "active"
    ).first()

    if existing_session:
        raise HTTPException(
            status_code=400,
            detail="Aktiv fokus sessiya mavjud"
        )

    new_session = FocusSession(
        user_id=user_id,
        duration=duration
    )

    db.add(new_session)
    db.commit()
    db.refresh(new_session)

    return new_session

def end_focus_session_service(db, session_id):

    focus_session = db.query(FocusSession).filter(
        FocusSession.id == session_id
    ).first()

    if not focus_session:
        raise HTTPException(
            status_code=404,
            detail="Fokus sessiya topilmadi"
        )

    if focus_session.status != "active":
        raise HTTPException(
            status_code=400,
            detail="Sessiya allaqachon tugagan"
        )

    focus_session.ended_at = datetime.utcnow()
    focus_session.status = "completed"

    db.commit()

    return focus_session

def get_focus_session_status_service(db, session_id):

    focus_session = db.query(FocusSession).filter(
        FocusSession.id == session_id
    ).first()

    if not focus_session:
        raise HTTPException(
            status_code=404,
            detail="Fokus sessiya topilmadi"
        )

    return focus_session

def get_focus_history_service(db, user_id):

    focus_sessions = db.query(FocusSession).filter(
        FocusSession.user_id == user_id
    ).order_by(FocusSession.started_at.desc()).all()

    return focus_sessions

def get_active_focus_session_service(db, user_id):

    active_session = db.query(FocusSession).filter(
        FocusSession.user_id == user_id,
        FocusSession.status == "active"
    ).first()

    return active_session

def cancel_focus_session_service(db, session_id):

    focus_session = db.query(FocusSession).filter(
        FocusSession.id == session_id
    ).first()

    if not focus_session:
        raise HTTPException(
            status_code=404,
            detail="Sessiya topilmadi"
        )

    focus_session.status = "cancelled"

    db.commit()

    return focus_session