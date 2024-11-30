from abc import ABC, abstractmethod

from db.db import users_crm


class AbstractRepository(ABC):
    @abstractmethod
    async def add_one():
        raise NotImplementedError

    @abstractmethod
    async def find_all():
        raise NotImplementedError


class MongoMotorRepository(AbstractRepository):
    collection_name = None

    async def add_one(self, data: dict):
        collection = users_crm.get_collection(self.collection_name)
        new_row = await collection.insert_one(data)
        return new_row.inserted_id

    async def find_all(self) -> list:
        collection = users_crm.get_collection(self.collection_name)
        data = await collection.find().to_list(1000)
        return data

    async def delete_all(self) -> int:
        collection = users_crm.get_collection(self.collection_name)
        result = await collection.delete_many({})
        return result.deleted_count
