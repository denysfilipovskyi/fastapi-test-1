from typing import Annotated

from bson import ObjectId

from api.dependencies import get_current_user, users_service
from fastapi import APIRouter, Depends, HTTPException, status
from schemas.users import UserSchema, UserSchemaAdd, UserSchemaUpdate
from services.users import UsersService

router = APIRouter(
    prefix='/users',
    tags=['Users'],
)


@router.patch('/{user_id}')
async def update_user(
    user_id: str,
    user: Annotated[UserSchemaUpdate, Depends()],
    users_service: Annotated[UsersService, Depends(users_service)],
    current_user: Annotated[UserSchemaUpdate, Depends(get_current_user)]
):
    if current_user.role != 'admin':
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='You are not authorized to perform this action'
        )

    if not ObjectId.is_valid(user_id):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f'Invalid ObjectId: {user_id}'
        )
    return await users_service.update_user_by_id(id=user_id, user=user)


@router.get('/{user_id}')
async def get_user(
    user_id: str,
    users_service: Annotated[UsersService, Depends(users_service)]
):
    if not ObjectId.is_valid(user_id):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f'Invalid ObjectId: {user_id}')

    return await users_service.get_user_by_id(user_id)


@router.delete('/{user_id}')
async def delete_user(
    user_id: str,
    users_service: Annotated[UsersService, Depends(users_service)],
):
    if not ObjectId.is_valid(user_id):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f'Invalid ObjectId: {user_id}')
    return await users_service.delete_user_by_id(user_id)


@router.get('')
async def get_users(
    users_service: Annotated[UsersService, Depends(users_service)]
):
    return await users_service.get_users()
