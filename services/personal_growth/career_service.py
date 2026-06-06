from db.models.personal_growth.career import (
    CareerInterest
)


def create_interest(
    db,
    data
):

    interest = CareerInterest(
        user_id=data.user_id,
        interest=data.interest
    )

    db.add(interest)

    db.commit()

    db.refresh(interest)

    return {
        "id": interest.id,
        "message": "Interest created"
    }


def get_interests(
    db,
    user_id
):

    return db.query(
        CareerInterest
    ).filter(
        CareerInterest.user_id == user_id
    ).all()


def delete_interest(
    db,
    interest_id
):

    interest = db.query(
        CareerInterest
    ).filter(
        CareerInterest.id == interest_id
    ).first()

    if not interest:
        return {
            "message": "Interest not found"
        }

    db.delete(interest)

    db.commit()

    return {
        "message": "Interest deleted"
    }