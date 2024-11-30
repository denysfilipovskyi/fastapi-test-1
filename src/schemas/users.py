from typing import Annotated, List, Optional
from pydantic import BaseModel, BeforeValidator, EmailStr, Field


PyObjectId = Annotated[str, BeforeValidator(str)]


class UserSchemaAdd(BaseModel):
    name: str = Field(...)
    email: EmailStr = Field(...)


class UserSchema(UserSchemaAdd):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)


class UserCollectionSchema(BaseModel):
    users: List[UserSchema]
