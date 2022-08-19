# Program to demonstrate the call of super() from __init__() of  a base class
class Base1(object): 
    def __init__(self):
        print("Base1 Class..")
        super(Base1, self).__init__()
class Base2(object): 
    def __init__(self):
        print("Base2 Class..")
class Derived(Base1, Base2): # Here, Derived is derived class from both Base1 & Base2 classes
    pass
D = Derived()
 
'''
OUTPUT:
Base1 Class..
Base2 Class..
'''
