from shopping_list import add_shopping_list, get_shopping_lists
from items import add_item, get_items, update_item, delete_item

def main():
    print("""
    1. Add shopping list
    2. List shopping list
    3. Add item
    4. List items
    5. Update item purchased status
    6. Delete item
    0. Exit
    """)
    while True:
        choice = input("Choose: ")

        match choice:
            case "1":
                add_shopping_list()
            case "2":
                get_shopping_lists()
            case "3":
                add_item()
            case "4":
                get_items()
            case "5":
                update_item()
            case "6":
                delete_item()
            case "0":
                print("Exiting...")
                break
            case _:
                print("Invalid choice")

if __name__=="__main__":
    main()