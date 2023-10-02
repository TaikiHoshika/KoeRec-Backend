from typing import Optional, TYPE_CHECKING
from sqlmodel import Field, SQLModel, Relationship
from datetime import datetime

if TYPE_CHECKING:
    from .user import User

class Token(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    token: str
    created_at: datetime = Field(default=datetime.utcnow(), nullable=False)

    user_id: Optional[int] = Field(default=None, foreign_key="user.id", unique=True)
    user: Optional["User"] = Relationship(back_populates="tokens")