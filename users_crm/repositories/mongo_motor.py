from db.mongo_motor import users_crm

from users_crm.repositories.abstract.nosql import AbstractNoSqlRepository


class MongoMotorRepository(AbstractNoSqlRepository):
    collection_name = None

    async def add_one(self, data: dict):
        collection = users_crm.get_collection(self.collection_name)
        new_row = await collection.insert_one(data)
        return new_row.inserted_id

    async def update_one(self, id, data: dict):
        collection = users_crm.get_collection(self.collection_name)
        await collection.find_one_and_update(
            {'_id': id},
            {'$set': data},
        )
        return await collection.find_one({'_id': id})

    async def find_one(self, filters: dict):
        collection = users_crm.get_collection(self.collection_name)
        return await collection.find_one(filters)

    async def find_by_filters(self, filters: dict):
        collection = users_crm.get_collection(self.collection_name)
        return await collection.find(filters).to_list(1000)

    async def delete(self, filters: dict = {}):
        collection = users_crm.get_collection(self.collection_name)
        result = await collection.delete_many(filters)
        return result.deleted_count
