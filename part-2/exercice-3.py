class Book:
    def __init__(self, title, author, year): 
        self.title = title
        self.author = author
        self.year = year

    def display_info(self):
        return f"'{self.title}' by {self.author.name} ({self.year})"

# __init__ hiya the constructor
# self hiya the object li raho being created
# display_info hiya method li taffichi les infos 3la the book

class Author:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        if not self.books:
            return f"{self.name} has no books."
        return f"Books by {self.name}: " + ", ".join([book.title for book in self.books])

# one-to-many relationship, one author → many books


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"{book.title} added to {self.name} Library.")

    def display_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            print(f"\nBooks available in {self.name} Library:")
            for book in self.books:
                print(f" - {book.display_info()}")
                
# same here, nothing special

class EBook(Book):
    def __init__(self, title, author, year, file_format):
        super().__init__(title, author, year)
        self.file_format = file_format

    def display_info(self):
        return f"'{self.title}' (eBook, {self.file_format}) by {self.author.name} ({self.year})"

# EBook(Book) means EBook inherits from Book, ay haja Book 3andha EBook tkoun 3ndhna SAUF ida n7ebou nbdlouha
# in this case we call Book the parent class or the base class or the superclass, and Ebook the child class or the derived class or the subclass (i just learned these terms lol)
# super().__init__(title, author, year) calls the constructor of the parent class to initialize the inherited attributes, ki tchouf lfo9 you'll find the Book have title, author, year
# self.file_format = file_format initializes the new attribute specific to EBook, which's el haja li zdnaha fl Ebook 
# display_info method in EBook overrides the one in Book to include the file format information

# Create authors
author1 = Author("Houcine Abdaoui")
author2 = Author("Yasser Bachta")

# Create books
book1 = Book("Overwatch", author1, 2024)
book2 = EBook("Hide & Seek", author2, 2023, "PDF")

# Link books to authors
author1.add_book(book1)
author2.add_book(book2)

# Create a library
maktabati = Library("Maktabati")

# Add books to the library
maktabati.add_book(book1)
maktabati.add_book(book2)

# Display information
maktabati.display_books()
print()
print(author1.display_books())
print(author2.display_books())