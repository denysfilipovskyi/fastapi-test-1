from users_crm.repositories.mongo_motor import MongoMotorRepository


class UserRepository(MongoMotorRepository):
    collection_name = 'users'
