#Create a book class with attributes like title,author and pages.Add a method to display the book's details.
class Book:
    """A simple attempt tp represent a book."""

    def __init__(self,title,author,pages):
        """Initialize the attributes of class Book."""
        self.title = title
        self.author = author
        self.pages = pages

    def book_details(self):
        """Dispaly the details of a specific book."""
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Page: {self.pages}")

my_book = Book('Python Crash Course','Eric Matthes','514')
my_book.book_details()
