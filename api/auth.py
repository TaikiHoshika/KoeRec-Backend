from sqlmodel import Session, select
from fastapi import APIRouter
from bcrypt import checkpw
from secrets import token_hex
from database import engine
from pydantic import BaseModel
import hmac
from hashlib import sha256
from datetime import datetime
from util import dateUtil
from settings import SECRET_KEY

from model import Token, User

router = APIRouter()

class Login(BaseModel):
    email: str
    password: str

@router.post("/auth/login/")
async def login(login: Login):    
    with Session(engine) as session:
        # メールアドレスが一致するユーザーを取得
        statement = select(User).where(User.email == login.email)
        user = session.exec(statement).one()

        # パスワードの一致確認
        if checkpw(login.password.encode(), user.password.encode()):
            generatedToken = token_hex()

            # トークンの発行
            # レコードがある場合は更新、ない場合は作成
            try:
                tokenStatement = select(Token).where(Token.user_id == user.id)
                token = session.exec(tokenStatement).one()

                token.token = generatedToken
                token.created_at = datetime.utcnow()
                session.add(token)
                session.commit()
            except:
                token = Token(token=generatedToken, user_id=user.id)
                session.add(token)
                session.commit()

            # 電子署名
            signature = hmac.new(
                SECRET_KEY.encode(),
                generatedToken.encode(),
                sha256
            ).digest()

            print(signature)

            # ログイン成功
            return {
                "isAuthenticated": True,
                "token": generatedToken,
                "time": dateUtil.getDateNow(datetime.utcnow())
            }

        else:
            # ログイン失敗
            return {"isAuthenticated": False}
