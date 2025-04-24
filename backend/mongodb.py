from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URI = "mongodb+srv://root:<root>@cluster0.he4luu0.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = AsyncIOMotorClient(MONGO_URI)
db = client["file_storage"]
collection = db["uploaded_files"]
