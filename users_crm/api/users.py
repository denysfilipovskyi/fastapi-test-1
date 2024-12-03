from typing import Annotated

from api.dependencies import require_admin_role, users_service, validate_object_id
from fastapi import APIRouter, Depends
from schemas.users import UserSchemaUpdate
from services.users import UsersService

router = APIRouter(
    prefix='/users',
    tags=['Users'],
)


@router.patch('/{user_id}')
async def update_user(
    user: Annotated[UserSchemaUpdate, Depends()],
    users_service: Annotated[UsersService, Depends(users_service)],
    _=Depends(require_admin_role),
    validated_user_id: str = Depends(validate_object_id)
):
    return await users_service.update_user_by_id(id=validated_user_id, user=user)


@router.get('/{user_id}')
async def get_user(
    users_service: Annotated[UsersService, Depends(users_service)],
    validated_user_id: str = Depends(validate_object_id)
):
    return await users_service.get_user_by_id(validated_user_id)


@router.delete('/{user_id}')
async def delete_user(
    users_service: Annotated[UsersService, Depends(users_service)],
    validated_user_id: str = Depends(validate_object_id)
):
    return await users_service.delete_user_by_id(validated_user_id)


@router.get('')
async def get_users(
    users_service: Annotated[UsersService, Depends(users_service)]
):
    return await users_service.get_users()
