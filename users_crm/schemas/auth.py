from typing import Literal
from pydantic import BaseModel, EmailStr, Field

from users_crm.schemas.users import UserSchemaAdd


class AuthSchema(UserSchemaAdd):
    email: EmailStr = Field(..., example='john.doe@example.com')
    password: str = Field(..., example='hashedpassword')
    role: Literal['admin', 'dev', 'simple mortal'] = Field(
        default='simple mortal')


class TokenSchema(BaseModel):
    access_token: str = Field(...)
    token_type: str = Field(...)


class LoginSchema(BaseModel):
    email: EmailStr = Field(..., example='john.doe@example.com')
    password: str = Field(..., example='hashedpassword')
