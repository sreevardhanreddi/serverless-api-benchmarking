import os

from motor.motor_asyncio import AsyncIOMotorClient


def get_db():
    db = AsyncIOMotorClient(os.getenv("MONGODB_URI"))
    try:
        yield db.sample_training
    finally:
        db.close()
