# Program to illustrate the use of private method
class test():
    def __init__(self, var):
        self.__var = var # Here var is private variable
    def __display(self): # Here display is private method
        print("From class method, Var = ", self.__var)        
obj = test(10)
obj._test__display()

'''
OUTPUT:
From class method, Var =  10
'''
