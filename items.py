from bson.objectid import ObjectId
from db import db



def add_item():
    list_name = input("Shopping list name: ")
    name = input("Item name: ")
    quantity = int(input("Quantity: "))
    tags = input("Tags: ").split(",")
    purchased = False

    shopping_list = db.shopping_list.find_one({"name": list_name})

    if not shopping_list:
        print("ERROR: Shopping list does not exist.")
        return

    shopping_list_id = shopping_list["_id"]

    result = db.items.insert_one({
        "name": name,
        "shopping_list_id": shopping_list_id,
        "quantity": quantity,
        "tags": tags,
        "purchased": purchased
    })

    print("Item added with ID:", result.inserted_id)


def get_items():
    for item in db.items.find():
        print(
            item["_id"],
            "-",
            item.get("name"),
            "| qty:",
            item.get("quantity"),
            "| purchased:",
            item.get("purchased")
        )

def update_item():
    item_id = input("Item ID to update: ")
    purchased = input("Purchased? (y/n): ").lower() == "y"

    result = db.items.update_one(
        {"_id": ObjectId(item_id)},
        {"$set": {"purchased": purchased}}
    )

    if result.matched_count:
        print("Item updated.")
    else:
        print("Item not found.")

def delete_item():
    item_id = input("Item ID to delete: ")
    db.items.delete_one({"_id": ObjectId(item_id)})
    print("Item deleted.")