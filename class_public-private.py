# Program illustrating the difference between public and private variables
class test():
    def __init__(self, var1, var2):
        self.var1 = var1
        self.__var2 = var2 # Here var2 is private variable
    def display(self):
        print("From class method, Var1 = ", self.var1)
        print("From class method, Var2 = ", self.__var2)
obj = test(10, 20)
obj.display()
print("From main module, Var1 = ", obj.var1)
print("From main module, Var2 = ", obj._test__var2)

'''
OUTPUT:
From class method, Var1 =  10
From class method, Var2 =  20
From main module, Var1 =  10
Traceback (most recent call last):
  File "C:/Users/admin/Downloads/CBIT OOPS USING PYTHON w.e.f. 13.06.2022/RMM OOPP LAB PROGRAMS/class_public-private.py", line 12, in <module>
    print("From main module, Var2 = ", obj.__var2)
AttributeError: 'test' object has no attribute '__var2'
'''
