class Book:
    def __init__(self, book_id, title):
        self.book_id = book_id
        self.title = title
        self.available = True


class Member:
    def __init__(self, name):
        self.name = name


class Library:
    def __init__(self):
        self.books = []

    def add_book(self):
        book_id = input("Enter Book ID: ")
        title = input("Enter Book Title: ")
        self.books.append(Book(book_id, title))

    def display_books(self):
        for b in self.books:
            status = "Available" if b.available else "Issued"
            print(b.book_id, b.title, status)

    def issue_book(self):
        book_id = input("Enter Book ID to issue: ")
        for b in self.books:
            if b.book_id == book_id and b.available:
                b.available = False
                print("Book Issued")
                return
        print("Book not available")

    def return_book(self):
        book_id = input("Enter Book ID to return: ")
        for b in self.books:
            if b.book_id == book_id:
                b.available = True
                print("Book Returned")
                return
        print("Book not found")


lib = Library()

while True:
    print("\n1.Add Book")
    print("2.Display Books")
    print("3.Issue Book")
    print("4.Return Book")
    print("5.Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        lib.add_book()
    elif ch == 2:
        lib.display_books()
    elif ch == 3:
        lib.issue_book()
    elif ch == 4:
        lib.return_book()
    elif ch == 5:
        break