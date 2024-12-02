from typing import Annotated
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from repositories.users import UserRepository
from services.users import UsersService
from services.auth import AuthService
from schemas.users import UserSchemaUpdate
from config import settings

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='auth/login')


def users_service():
    return UsersService(UserRepository)


def auth_service():
    return AuthService(UserRepository)


async def get_current_user(
        users_service: Annotated[UsersService, Depends(users_service)],
        token: str = Depends(oauth2_scheme)) -> UserSchemaUpdate:
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        email: str = payload.get('sub')
        if email is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid token')

        user = await users_service.get_user({'email': email})
        if not user:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='User not found')

        return user
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid token')
