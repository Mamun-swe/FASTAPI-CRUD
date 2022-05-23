

from typing import Optional
from pydantic import BaseModel, EmailStr, Field


class UserSchema(BaseModel):
    name: str = Field(...)
    email: EmailStr = Field(...)
    phone: str = Field(...)
    address: str = Field(...)


class UpdateUserModel(BaseModel):
    name: Optional[str]
    email: Optional[EmailStr]
    phone: Optional[str]
    address: Optional[str]


def ResponseModel(data):
    return {
        "code": 200,
        "status": True,
        "data": [data]
    }


def ErrorResponseModel(errors, code):
    return{
        "code": code,
        "status": False,
        "errors": {"message": errors}
    }
