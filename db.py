import os

from pymongo import MongoClient

MONGODB_URI = os.getenv("MONGODB_URI") or "mongodb://localhost:27017"
DB_NAME = os.getenv("MONGODB_DB") or "library"

client = MongoClient(MONGODB_URI)
db = client[DB_NAME]