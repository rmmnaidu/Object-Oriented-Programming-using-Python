# EX-2. Program to implement multiple inheritance
class Base1: #First Base Class
    def __init__(self):
        super(Base1,self).__init__()
        print("Base1 Class..")
class Base2:#Second Base Class
    def __init__(self):
        super(Base2,self).__init__()
        print("Base2 Class..")
class Derived(Base1, Base2): #Derived class derived from 2 base classes Base1 & Base2
    def __init__(self):
        super(Derived,self).__init__()
        print("Derived Class..")
        print(Derived.__mro__)
Derived()
'''
OUTPUT:
Base2 Class..
Base1 Class..
Derived Class..
'''
