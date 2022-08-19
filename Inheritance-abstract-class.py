# Program to demonstrate the concept of abstract class
class Fruit:
    def taste(self):
        raise NotImplementedError()
    def rich_in(self):
        raise NotImplementedError()
    def colour(self):
        raise NotImplementedError()
class Mango(Fruit):
    def taste(self):
        return "Sweet"
    def rich_in(self):
        return "Vitamin A"
    def colour(self):
        return "Yellow"
class Orange(Fruit):
    def taste(self):
        return "Sour"
    def rich_in(self):
        return "Vitamin C"
    def colour(self):
        return "Orange"
m = Mango()
print("Mango fruit taste is ",m.taste(),", it contains ",m.rich_in(),"and its colour is ",m.colour())
o = Orange()
print("Orange fruit taste is ",o.taste(),", it contains ",o.rich_in(),"and its colour is ",o.colour())

'''
OUTPUT:
Mango fruit taste is  Sweet , it contains  Vitamin A and its colour is  Yellow
Orange fruit taste is  Sour , it contains  Vitamin C and its colour is  Orange
'''
