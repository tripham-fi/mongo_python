from bson.objectid import ObjectId
from db import db


def add_book():
    title = input("Title: ")
    author = input("Author: ")
    year = int(input("Year: "))
    copies = int(input("Copies: "))
    ebook = input("Ebook? (y/n): ").lower() == "y"


    book = {
        "title": title,
        "author": author,
        "year": year,
        "copies": copies,
        "ebook": ebook
    }

    result = db.books.insert_one(book)
    print("Book added with ID:", result.inserted_id)


def list_books():
    for book in db.books.find():
        print(
            book["_id"], "-", book.get("title"), "-", book.get("author"), "| copies:", book.get("copies")
        )


def find_book_by_id():
    book_id = input("Book ID: ")
    book = db.books.find_one({"_id": ObjectId(book_id)})

    if book:
        print(book)
    else:
        print("Book not found.")


def update_book():
    book_id = input("Book ID to update: ")
    copies = int(input("New number of copies: "))

    result = db.books.update_one(
        {"_id": ObjectId(book_id)},
        {"$set": {"copies": copies}}
    )

    if result.matched_count:
        print("Book updated.")
    else:
        print("Book updated failed, no match or wrong field.")


def delete_book():
    book_id = input("Book ID to delete: ")
    db.books.delete_one({"_id": ObjectId(book_id)})
    print("Book deleted.")