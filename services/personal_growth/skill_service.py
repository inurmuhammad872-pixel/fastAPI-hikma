from db.models.personal_growth.skill import Skill


def create_skill(db, data):

    skill = Skill(
        user_id=data.user_id,
        name=data.name,
        score=data.score
    )

    db.add(skill)

    db.commit()

    db.refresh(skill)

    return {
        "id": skill.id,
        "message": "Skill created"
    }


def get_skills(db, user_id):

    return db.query(
        Skill
    ).filter(
        Skill.user_id == user_id
    ).all()


def update_skill(db, skill_id, score):

    skill = db.query(
        Skill
    ).filter(
        Skill.id == skill_id
    ).first()

    if not skill:
        return {
            "message": "Skill not found"
        }

    skill.score = score

    db.commit()

    return {
        "message": "Skill updated"
    }


def delete_skill(db, skill_id):

    skill = db.query(
        Skill
    ).filter(
        Skill.id == skill_id
    ).first()

    if not skill:
        return {
            "message": "Skill not found"
        }

    db.delete(skill)

    db.commit()

    return {
        "message": "Skill deleted"
    }