from pydantic import BaseModel, EmailStr, Field


class TokenSchema(BaseModel):
    access_token: str = Field(...)
    token_type: str = Field(...)


class LoginSchema(BaseModel):
    email: EmailStr = Field(..., example='john.doe@example.com')
    password: str = Field(..., example='hashedpassword')
