from typing import Annotated

from api.dependencies import auth_service
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from users_crm.schemas.auth import TokenSchema
from users_crm.schemas.users import UserSchema, UserSchemaAddInput
from users_crm.services.auth import AuthService

router = APIRouter(
    prefix='/auth',
    tags=['Auth'],
)


@router.post('/register', response_model=UserSchema)
async def add_user(
    auth_data: Annotated[UserSchemaAddInput, Depends()],
    auth_service: Annotated[AuthService, Depends(auth_service)],
):
    return await auth_service.register_user(auth_data)


@router.post('/login', response_model=TokenSchema)
async def login_user(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    auth_service: Annotated[AuthService, Depends(auth_service)]
):
    token = await auth_service.login_user(
        {'email': form_data.username, 'password': form_data.password}
    )
    return token
