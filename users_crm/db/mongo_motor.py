from config import settings
from motor.motor_asyncio import AsyncIOMotorClient

client = AsyncIOMotorClient(settings.MONGO_URI)
users_crm = client.get_database(settings.DATABASE_NAME)
