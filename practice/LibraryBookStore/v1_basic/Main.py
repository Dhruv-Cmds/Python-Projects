
# Author: Dhruv
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_issued = False


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        self.books.append(Book(title, author))
        print("✅ Book added")

    def list_books(self):
        if not self.books:
            print("❌ No books in library")
            return

        for i, book in enumerate(self.books, 1):
            status = "Issued" if book.is_issued else "Available"
            print(f"{i}. {book.title} by {book.author} [{status}]")

    def issue_book(self, title):
        for book in self.books:
            if book.title == title and not book.is_issued:
                book.is_issued = True
                print("✅ Book issued")
                return
        print("❌ Book not available")

    def return_book(self, title):
        for book in self.books:
            if book.title == title and book.is_issued:
                book.is_issued = False
                print("✅ Book returned")
                return
        print("❌ Book not found or not issued")


# -------- MENU SYSTEM --------

lib = Library()

while True:
    print("\n===== Library Menu =====")
    print("1. Add Book")
    print("2. Show Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        title = input("Book title: ")
        author = input("Author: ")
        lib.add_book(title, author)

    elif choice == "2":
        lib.list_books()

    elif choice == "3":
        title = input("Book title to issue: ")
        lib.issue_book(title)

    elif choice == "4":
        title = input("Book title to return: ")
        lib.return_book(title)

    elif choice == "5":
        print("Goodbye 👋")
        break

    else:
        print("❌ Invalid choice")
