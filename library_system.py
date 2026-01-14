# Library Management System - CRUD Framework

library_books = []

def create_book():
    print("\n--- Add New Book ---")
    title = input("Enter Book Title: ")
    author = input("Enter Author: ")
    status = "Available"
    
    book = {
        "title": title,
        "author": author,
        "status": status
    }
    library_books.append(book)
    print(f"Book '{title}' added successfully!")

def read_books():
    print("\n--- Current Library Collection ---")
    if not library_books:
        print("The library is currently empty.")
    else:
        for index, book in enumerate(library_books, start=1):
            print(f"{index}. Title: {book['title']} | Author: {book['author']} | Status: {book['status']}")

def update_book():
    read_books()
    if library_books:
        try:
            choice = int(input("\nEnter the book number to update status: ")) - 1
            if 0 <= choice < len(library_books):
                new_status = input("Enter new status (Available/Checked Out): ")
                library_books[choice]['status'] = new_status
                print("Book updated successfully!")
            else:
                print("Invalid selection.")
        except ValueError:
            print("Please enter a valid number.")

def delete_book():
    read_books()
    if library_books:
        try:
            choice = int(input("\nEnter the book number to delete: ")) - 1
            if 0 <= choice < len(library_books):
                removed = library_books.pop(choice)
                print(f"Removed: {removed['title']}")
            else:
                print("Invalid selection.")
        except ValueError:
            print("Please enter a valid number.")

def main_menu():
    while True:
        print("\n=== LIBRARY SYSTEM MENU ===")
        print("1. Add Book (Create)")
        print("2. View Books (Read)")
        print("3. Update Status (Update)")
        print("4. Remove Book (Delete)")
        print("5. Exit")
        
        choice = input("Select an option: ")
        
        if choice == '1': create_book()
        elif choice == '2': read_books()
        elif choice == '3': update_book()
        elif choice == '4': delete_book()
        elif choice == '5': 
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main_menu()