# Program to call a class method from another method of the same class
class test():
    def __init__(self, var):
        self.var = var 
    def display(self): 
        print("Var is = ", self.var)
    def add_2(self):
        self.var+=2
        self.display() # Here, display() method is called in method add_2()
obj = test(10)
obj.add_2()

'''
OUTPUT:
Var is =  12
'''
