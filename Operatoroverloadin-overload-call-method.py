# Program to overload the __call__() method
class Mult:
    def __init__(self, num):
        self.num = num
    def __call__(self, o1):
        return self.num*o1
x = Mult(100)
print(x(4))

'''
OUTPUT:
400
'''

        
       
