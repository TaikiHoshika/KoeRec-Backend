from sqlmodel import Session, select
from fastapi import APIRouter
from bcrypt import checkpw
from secrets import token_hex
from database import engine
from pydantic import BaseModel

from model import Token, User

router = APIRouter()

class Login(BaseModel):
    email: str
    password: str

@router.post("/auth/login/")
def login(login: Login):    
    with Session(engine) as session:
        statement = select(User).where(User.email == login.email)
        user = session.exec(statement).one()

        if checkpw(login.password.encode(), user.password.encode()):
            generatedToken = token_hex()

            try:
                authenticate = Token(token=generatedToken, user_id=user.id)
                session.add(authenticate)
                session.commit()
            except:
                tokenStatement = select(Token).where(Token.user_id == user.id)
                token = session.exec(tokenStatement).first()

                token.token = generatedToken
                session.add(token)
                session.commit()

            return {"isAuthenticated": False, "token": generatedToken}

        else:
            return {"isAuthenticated": False}
