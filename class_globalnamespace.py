# Program to shows how a class method calls a function defined in the global namespace
def scale_10(x):
    return x*10
class test():
    def __init__(self, var):
        self.var = var
    def display(self):
        print("Var is = ", self.var)
    def modify(self):
        self.var = scale_10(self.var)
        
obj = test(10)
obj.display()
obj.modify()
obj.display()

'''
OUTPUT:
Var is =  10
Var is =  100
'''
