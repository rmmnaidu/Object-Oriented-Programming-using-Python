# Program to demonstrate the issue of invoking __init__() case of multiple inheritance
class Base1(object): # Here, Base1 is Base or Master or Parent class
    def __init__(self):
        print("Base1 Class..")
class Base2(object): 
    def __init__(self):
        print("Base2 Class..")
class Derived(Base1, Base2): # Here, Derived is derived class from both Base1 & Base2 classes
    pass
D = Derived()
 
'''
OUTPUT:
Base1 Class..
'''
