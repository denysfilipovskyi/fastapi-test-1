from utils.repository import MongoMotorRepository


class UserRepository(MongoMotorRepository):
    collection_name = 'users'
