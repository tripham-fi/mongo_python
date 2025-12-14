from books import (
    add_book,
    list_books,
    find_book_by_id,
    update_book,
    delete_book
)

def main():
    print("""
    1. Add book
    2. List books
    3. Update book copies
    4. Delete book
    0. Exit
    """)
    while True:
        choice = input("Choose: ")

        match choice:
            case "1":
                add_book()
            case "2":
                list_books()
            case "3":
                update_book()
            case "4":
                delete_book()
            case "0":
                print("Exiting...")
                break
            case _:
                print("Invalid choice")

if __name__=="__main__":
    main()