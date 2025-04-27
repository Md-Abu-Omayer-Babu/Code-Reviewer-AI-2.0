from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URI = "mongodb://localhost:27017"

client = AsyncIOMotorClient(MONGO_URI)
db = client["file_storage"]
collection = db["uploaded_files"]
