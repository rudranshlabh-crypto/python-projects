class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True  # Tracks availability

    def borrow_book(self):
        if self.is_available:
            self.is_available = False
            print(f"Success: You have borrowed '{self.title}'.")
            return True
        else:
            print(f"Error: '{self.title}' is currently unavailable.")
            return False

    def return_book(self):
        if not self.is_available:
            self.is_available = True
            print(f"Success: Thank you for returning '{self.title}'.")
            return True
        else:
            print(f"Notice: '{self.title}' was already in the library.")
            return False


class Library:
    def __init__(self):
        self.books = []  # Stores book objects

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        print("\n--- Library Catalog ---")
        if not self.books:
            print("The library is empty.")
            return
        for book in self.books:
            status = "Available" if book.is_available else "Borrowed"
            print(f"'{book.title}' by {book.author} [{status}]")
        print("-----------------------\n")

    def find_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        print(f"Error: '{title}' not found in this library.")
        return None


my_library = Library()

my_library.add_book(Book("The Hobbit", "J.R.R. Tolkien"))
my_library.add_book(Book("1984", "George Orwell"))

my_library.display_books()

target_book = my_library.find_book("1984")
if target_book:
    target_book.borrow_book()

my_library.display_books()

if target_book:
    target_book.borrow_book()

if target_book:
    target_book.return_book()
Use code with cautio