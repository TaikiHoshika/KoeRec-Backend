from sqlmodel import Session
from database import engine
from model import Plan, User


def create_plans():
    with Session(engine) as session:
        plan_1 = Plan(name="Private Plan", storage=100)
        plan_2 = Plan(name="Team Plan", storage=500)

        user_1 = User(name="Taiki Hoshika", email="taiki@example.com", password="$2b$12$0eN/HbCubpJuwmSdhtjLiuxE7jRDuGia8ABMckM46WTWYcpl0QaZO", plan=plan_1)
        user_2 = User(name="Hikari Hoshika", email="hikari@example.com", password="$2b$12$0eN/HbCubpJuwmSdhtjLiuxE7jRDuGia8ABMckM46WTWYcpl0QaZO", plan=plan_2)
        session.add(user_1)
        session.add(user_2)
        session.commit()

        session.refresh(plan_1)
        session.refresh(plan_2)
        session.refresh(user_1)
        session.refresh(user_2)

        print(plan_1)
        print(plan_2)
        print(user_1)
        print(user_2)


def main():
    create_plans()


if __name__ == "__main__":
    main()