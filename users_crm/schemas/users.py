from datetime import datetime, timezone
from typing import List, Literal, Optional
from pydantic import BaseModel, ConfigDict, EmailStr, Field, SecretStr

from users_crm.schemas.types import PyObjectId


class UserBaseSchema(BaseModel):
    first_name: str = Field(..., example='Den')
    last_name: Optional[str] = Field('', example='Smith')
    role: Literal['admin', 'dev', 'simple mortal'] = Field(
        default='simple mortal')


class UserSchemaAdd(UserBaseSchema):
    email: EmailStr = Field(..., example='john.doe@example.com')
    password: str = SecretStr(...)


class UserSchemaUpdate(UserBaseSchema):
    first_name: Optional[str] = Field('', example='John')
    is_active: bool = Field(default=True, example=True)

    model_config = ConfigDict(
        populate_by_name=True
    )


class UserSchema(UserBaseSchema):
    id: Optional[PyObjectId] = Field(alias='_id', default=None)
    email: EmailStr = Field(..., example='john.doe@example.com')
    is_active: bool = Field(default=True, example=True)
    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        example='2023-01-01T00:00:00Z'
    )
    last_login: Optional[datetime] = Field(default=None, example='2023-01-02T00:00:00Z')

    model_config = ConfigDict(
        populate_by_name=True,
        json_encoders={PyObjectId: str}
    )


class UserCollectionSchema(BaseModel):
    users: List[UserSchema]
