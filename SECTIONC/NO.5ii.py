# creating a derived class

class EBook:
    def __init__(self):
        self.formate = []   
    def derived_book(display, title, author,format):
        display.format.append({'title': title, 'author': author, 'format': format})
        print(f'The most interesting book is known  as ' + display.title, 'wrote by '+ display.author,  + display.pages,'pages and its' + display.format)
p1 = EBook('Listen but do not judge','N.edith', 120, '16th version')
p1.derived_book()
        
