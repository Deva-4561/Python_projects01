class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append({"title": book, "issued": False})
        print(f'"{book}" added to library.')

    def view_books(self):
        if not self.books:
            print("No books in library.")
            return
        
        print("\nLibrary Books:")
        for i, book in enumerate(self.books, 1):
            status = "Issued" if book["issued"] else "Available"
            print(f"{i}. {book['title']} - {status}")

    def issue_book(self, book_title):
        for book in self.books:
            if book["title"].lower() == book_title.lower():
                if not book["issued"]:
                    book["issued"] = True
                    print(f'You issued "{book_title}".')
                    return
                else:
                    print("Book already issued.")
                    return
        print("Book not found.")

    def return_book(self, book_title):
        for book in self.books:
            if book["title"].lower() == book_title.lower():
                if book["issued"]:
                    book["issued"] = False
                    print(f'You returned "{book_title}".')
                    return
                else:
                    print("Book was not issued.")
                    return
        print("Book not found.")


library = Library()

while True:
    print("\n--- Library Menu ---")
    print("1. Add Book")
    print("2. View Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        book = input("Enter book name: ")
        library.add_book(book)

    elif choice == '2':
        library.view_books()

    elif choice == '3':
        book = input("Enter book name to issue: ")
        library.issue_book(book)

    elif choice == '4':
        book = input("Enter book name to return: ")
        library.return_book(book)

    elif choice == '5':
        print("Exiting...")
        break

    else:
        print("Invalid choice. Try again.")