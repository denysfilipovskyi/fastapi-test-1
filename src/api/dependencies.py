from repositories.users import UserRepository
from services.users import UsersService


def users_service():
    return UsersService(UserRepository)
