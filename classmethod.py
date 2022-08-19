# Program to demonstrate the use of classmethod
class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        return self.length * self.breadth
    @classmethod # Class mthod
    def Square(cls, side):
        return cls(side, side)
S = Rectangle.Square(10)
print("Area = ", S.area())

'''
OUTPUT:
Area =  100
'''

    
