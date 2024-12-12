# creating a function

class Book:
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages
    def remove_book(self, pages):
        self.books = [book for book in self.books if book['pages'] != pages]
        return('book title and author')
P1 = Book()


