# Program to demonstrate the use of built-in class attributes
class test():
    def __init__(self, var1, var2):
        self.var1 = var1
        self.var2 = var2
    def display(self):
        print("Var1 is = ", self.var1)
        print("Var2 is = ", self.var2)
obj = test(10, 2.5)
obj.display()
print("object.__dict__ =", obj.__dict__)
print("object.__doc__ =", obj.__doc__)
print("class.__name__ =", test.__name__)
print("object.__module__ =", obj.__module__)
print("class.__bases__ =", test.__bases__)
'''
OUTPUT:
Var1 is =  10
Var2 is =  2.5
object.__dict__ = {'var1': 10, 'var2': 2.5}
object.__doc__ = None
class.__name__ = test
object.__module__ = __main__
class.__bases__ = (<class 'object'>,)
'''
