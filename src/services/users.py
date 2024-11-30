# from models.users import User
from schemas.users import UserCollectionSchema, UserSchemaAdd
from utils.repository import AbstractRepository


class UsersService:
    def __init__(self, users_repo: AbstractRepository):
        self.users_repo: AbstractRepository = users_repo()

    async def add_user(self, user: UserSchemaAdd):
        user_dict = user.model_dump(by_alias=True, exclude=['id'])
        user_id = await self.users_repo.add_one(user_dict)
        return user_id

    async def get_users(self):
        users = await self.users_repo.find_all()
        return UserCollectionSchema(users=users)

    async def delete_all_users(self) -> int:
        return await self.users_repo.delete_all()
