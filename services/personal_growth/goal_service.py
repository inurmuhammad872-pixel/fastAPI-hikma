from db.models.personal_growth.goal import Goal


def create_goal(db, data):

    goal = Goal(
        user_id=data.user_id,
        title=data.title
    )

    db.add(goal)
    db.commit()
    db.refresh(goal)

    return {
        "id": goal.id,
        "message": "Goal created"
    }


def get_goals(db, user_id):

    return db.query(
        Goal
    ).filter(
        Goal.user_id == user_id
    ).all()


def update_goal(
    db,
    goal_id,
    completed
):

    goal = db.query(
        Goal
    ).filter(
        Goal.id == goal_id
    ).first()

    if not goal:
        return {
            "message": "Goal not found"
        }

    goal.completed = completed

    db.commit()

    return {
        "message": "Goal updated"
    }


def delete_goal(
    db,
    goal_id
):

    goal = db.query(
        Goal
    ).filter(
        Goal.id == goal_id
    ).first()

    if not goal:
        return {
            "message": "Goal not found"
        }

    db.delete(goal)

    db.commit()

    return {
        "message": "Goal deleted"
    }