# defining a python class 
class Book:
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages
    def display_book(display):
        print(f'The most interesting book is known  as ' + display.title, 'wrote by '+ display.author,  + display.pages,'pages')
p1 = Book('Listen but do not judge','N.edith', 120)
p1.display_book()
        
        
