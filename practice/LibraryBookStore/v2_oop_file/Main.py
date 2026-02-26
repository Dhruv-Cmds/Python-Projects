class BookStore:
    
    def __init__(self, author, title, is_issued=False):
        self.author = author
        self.title = title
        self.is_issued = is_issued

class Library:

    filepath = "library.txt"

    def __init__(self):
        self.books = []
        self.load()
        
    def save(self):     
        with open (self.filepath , "w") as f:
            for book in self.books:
                f.write(f"{book.title}|{book.author}|{book.is_issued}\n")

    def load(self):
        try:
            with open(self.filepath, "r") as f:
                for line in f:
                    title, author, is_issued = line.strip().split("|")
                    self.books.append(
                        BookStore(author, title, is_issued == "True")
                    )
        except FileNotFoundError:
            self.save()
    
    def add_book (self , title , author):
        self.books.append(BookStore(author , title))
        self.save()
        print("Book added")
    
    def available_books(self):
        if not self.books:
            print("No book found.")
            return
        
        for i , book in enumerate(self.books , 1):
            status = "Issued" if book.is_issued else "Available"
            print(f"{i}. {book.title} by {book.author} [{status}]")

    def issue_book(self , title):
        for book in self.books:
            if book.title == title and not book.is_issued:
                book.is_issued = True
                self.save()
                print("✅ Book issued")
                return
        print("❌ Book not available")

    def return_book(self, title):
        for book in self.books:
            if book.title == title and book.is_issued:
                book.is_issued = False
                self.save()
                print("✅ Book returned")
                return
        print("❌ Book not found or not issued")

    def menu (self):
        while True:
            print("\n===== Library Menu =====")
            print("1. Add Book")
            print("2. Show Books")
            print("3. Issue Book")
            print("4. Return Book")
            print("5. Exit")
            
            try:
                choice = int(input("Enter your choice: "))
            except ValueError:
                print("Invalid choice type!")
                continue

            if choice == 1:
               title = input("Book title: ")
               author = input("Author: ")
               self.add_book(title , author)
            
            elif choice == 2:
                self.available_books()
            
            elif choice == 3:
                title = input("Book title to issue: ")
                self.issue_book(title)
            
            elif choice == 4:
                title = input("Book title to return: ")
                self.return_book(title)
            
            elif choice == 5:
                print("Thank you for using us! Have a nice day!")
                break
            
            else:
                print("Invalid choice rang!")

l = Library()
l.menu()