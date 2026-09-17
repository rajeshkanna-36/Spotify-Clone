from datetime import date
from typing import Optional

from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    user_name: str
    email_id: EmailStr
    mobile_number: Optional[str] = None
    date_of_birth: Optional[date] = None
    password: str


class Token(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str


class UserProfile(BaseModel):
    user_id: int
    user_name: str
    email_id: str
    mobile_number: Optional[str] = None
    date_of_birth: Optional[date] = None

    class Config:
        from_attributes = True


class RefreshTokenRequest(BaseModel):
    refresh_token: str
