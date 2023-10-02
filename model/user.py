from typing import Optional, TYPE_CHECKING, List
from sqlmodel import Field, SQLModel, Relationship
from datetime import datetime

if TYPE_CHECKING:
    from .plan import Plan
    from .token import Token

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    email: str = Field(index=True)
    password: str
    created_at: datetime = Field(default=datetime.utcnow(), nullable=False)
    updated_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)

    plan_id: Optional[int] = Field(default=None, foreign_key="plan.id")
    plan: Optional["Plan"] = Relationship(back_populates="users")

    tokens: List["Token"] = Relationship(back_populates="user")