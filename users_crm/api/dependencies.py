from typing import Annotated, List
from bson import ObjectId
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from repositories.users import UserRepository
from services.users import UsersService
from services.auth import AuthService
from users_crm.schemas.users import UserSchemaUpdate

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='auth/login')


def users_service():
    return UsersService(UserRepository)


def auth_service():
    return AuthService(UserRepository)


async def get_current_user(
        auth_service: Annotated[AuthService, Depends(auth_service)],
        token: str = Depends(oauth2_scheme)):
    return await auth_service.get_user_by_token(token)


def require_admin_role(
    current_user: Annotated[UserSchemaUpdate, Depends(get_current_user)]
):
    if current_user.role not in ['admin']:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='You are not authorized to perform this action'
        )
    return current_user


def validate_object_id(user_id: str):
    if not ObjectId.is_valid(user_id):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f'Invalid ObjectId: {user_id}'
        )
    return user_id
