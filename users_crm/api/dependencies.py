from typing import Annotated
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from repositories.users import UserRepository
from services.users import UsersService
from services.auth import AuthService

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='auth/login')


def users_service():
    return UsersService(UserRepository)


def auth_service():
    return AuthService(UserRepository)


async def get_current_user(
        auth_service: Annotated[AuthService, Depends(auth_service)],
        token: str = Depends(oauth2_scheme)):
    return await auth_service.get_user_by_token(token)
