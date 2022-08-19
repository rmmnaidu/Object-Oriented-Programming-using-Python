# Program to call the __init__() methods of all the classes.
class Base1(object): 
    def __init__(self):
        print("Base1 Class..")
        super(Base1, self).__init__()
class Base2(object): 
    def __init__(self):
        print("Base2 Class..")
class Derived(Base1, Base2): # Here, Derived is derived class from both Base1 & Base2 classes
    def __init__(self):
        super(Derived, self).__init__()
        print("Derived Class..")
D = Derived()
 
'''
OUTPUT:
Base1 Class..
Base2 Class..
Derived Class..
'''
