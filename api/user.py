from sqlmodel import Session, select
from fastapi import APIRouter
from database import engine

from model import User, Plan

router = APIRouter()

@router.post("/user/create/")
def create_user(user: User):
    with Session(engine) as session:
        session.add(user)
        session.commit()
        session.refresh(user)
        return user

@router.get("/user/get/")
def get_user():
    with Session(engine) as session:
        users = session.exec(select(User)).all()
        return users

@router.get("/user/get/{id}/")
def get_a_user(id):
    with Session(engine) as session:
        statement = select(User).where(User.id == id)
        user = session.exec(statement).one()

        statement = select(Plan).where(Plan.id == user.plan_id)
        plan = session.exec(statement).first()

        result = {
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "updated_at": user.updated_at,
            "created_at": user.created_at,
            "plan": {
                "id": plan.id,
                "name": plan.name,
                "storage": plan.storage
            }
        }

        return result