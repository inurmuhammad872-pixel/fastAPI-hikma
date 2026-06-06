from db.models.personal_growth.discipline import (
    Habit,
    HabitLog
)

from datetime import date
def create_habit(db, data):

    habit = Habit(
        user_id=data.user_id,
        name=data.name
    )

    db.add(habit)

    db.commit()

    db.refresh(habit)

    return {
        "id": habit.id,
        "message": "Habit created"
    }
def get_habits(db, user_id):

    return db.query(
        Habit
    ).filter(
        Habit.user_id == user_id
    ).all()


def toggle_habit(
    db,
    habit_id,
    completed
):

    today = date.today()

    log = db.query(
        HabitLog
    ).filter(
        HabitLog.habit_id == habit_id,
        HabitLog.date == today
    ).first()

    if not log:

        log = HabitLog(
            habit_id=habit_id,
            date=today,
            completed=completed
        )

        db.add(log)

    else:

        log.completed = completed

    db.commit()

    return {
        "message": "Updated"
    }