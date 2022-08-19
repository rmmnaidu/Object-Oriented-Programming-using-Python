# Program to compare two objects of user-defined class type.
class Book:
    def __init__(self):
        title = ""
        publisher = ""
        price = 0
    def set(self, title, publisher, price):
        self.title = title
        self.publisher = publisher
        self.price = price
    def display(self):
        print("Title:",self.title)
        print("Publisher:",self.publisher)
        print("price:",self.price)
    def __gt__(self, B):
        if self.price > B.price:
            return True
        else:
            return False
B1 = Book()
B1.set("OOP uisng Python", "Oxford University Press", 625)
B2 = Book()
B2.set("Letus Python", "BPB", 600)
if B1>B2:
    print("This book has more solved example problems, so I will prefer to buy..")
    B1.display()
    
'''
OUTPUT:
This book has more solved example problems, so I will prefer to buy..
Title: OOP uisng Python
Publisher: Oxford University Press
price: 625
'''

