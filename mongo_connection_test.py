import os

from bson import ObjectId
from pymongo import MongoClient

MONGODB_URI = os.getenv("MONGODB_URI") or "mongodb://localhost:27017"
DB_NAME = os.getenv("MONGODB_DB") or "library"
client = MongoClient(MONGODB_URI)
db = client[DB_NAME]

print("Collections:", db.list_collection_names())
print("Books in database:\n")

for book in db.books.find().limit(5):
    print(book.get("title"), "-", book.get("author"))

book_id_to_find = "6780b2d277f48b749b940ee4"

db.books.find_one({ "_id": ObjectId(book_id_to_find) })


def add_book():
    author = input("Author:")
    title = input("Title: ")
    year = int(input("Year: "))

    book = {
        "title": title,
        "author": author,
        "year": year
    }

    result = db.books.insert_one(book)
    return result.inserted_id

_id = add_book()
print("\nInserted document ID:", _id)