from fastapi import HTTPException, status
from schemas.users import PyObjectId, UserCollectionSchema, UserSchema, UserSchemaUpdate

from users_crm.repositories.abstract.nosql import AbstractNoSqlRepository


class UsersService:
    def __init__(self, users_repo: AbstractNoSqlRepository):
        self.users_repo: AbstractNoSqlRepository = users_repo()

    async def update_user_by_id(self, id: str, user: UserSchemaUpdate) -> UserSchema:
        user_dict = user.model_dump(by_alias=True)
        data = await self.users_repo.update_one(
            id=PyObjectId(id),
            data=user_dict
        )
        if not data:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')
        return UserSchema(**data)

    async def get_user_by_id(self, id: str) -> UserSchema:
        data = await self.users_repo.find_one({'_id': PyObjectId(id)})
        if not data:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')
        return UserSchema(**data)

    async def get_users(self, filters: dict = {}) -> UserCollectionSchema:
        users = await self.users_repo.find_by_filters(filters)
        return UserCollectionSchema(users=users)

    async def get_user(self, filters: dict = {}) -> UserSchema:
        data = await self.users_repo.find_one(filters)
        if not data:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')
        return UserSchema(**data)

    async def delete_user_by_id(self, id: str) -> int:
        return await self.users_repo.delete({'_id': PyObjectId(id)})
