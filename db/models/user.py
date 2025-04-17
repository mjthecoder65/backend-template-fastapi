from datetime import datetime

from pydantic import EmailStr
from sqlmodel import Field, SQLModel


class UserBase(SQLModel):
    username: str = Field(max_length=50, unique=True)
    email: EmailStr = Field(max_length=100, unique=True)


class UserCreate(UserBase):
    password: str = Field(min_length=8, max_length=128)


class User(UserBase, table=True):
    __tablename__ = "users"

    id: int | None = Field(default=None, primary_key=True)
    last_login_at: datetime | None = Field(default=None, nullable=True)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now, nullable=True)
    password_hash: str

    def __repr__(self) -> str:
        return f"User(id={self.id}, username={self.username}, email={self.email})"


class UserResponse(UserBase):
    id: int
    last_login_at: datetime | None = Field(default=None, nullable=True)
    created_at: datetime
    updated_at: datetime = Field(default=None, nullable=True)

    class Config:
        from_attributes = True
