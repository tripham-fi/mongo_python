from db import db


def add_shopping_list():
    name = input("List name: ")
    store = input("Store: ")
    shopper = input("Shopper: ")
    budget = int(input("Budget: "))
    completed = False

    result = db.shopping_list.insert_one({
        "name": name,
        "store": store,
        "shopper": shopper,
        "budget": budget,
        "complete": completed
    })

    print("Shopping list added with ID:", result.inserted_id)

def get_shopping_lists():
    for shoppingList in db.shopping_list.find():
        print(
            shoppingList["_id"],
            "-",
            shoppingList.get("name"),
            "| store:",
            shoppingList.get("store"),
            "| completed:",
            shoppingList.get("complete")
        )