# Program to implement single inheritance
class A:
    def m1(self):
        print("m1 is method of Main or Base Class A..")
class B(A): # Class B is derived from the Parent or Base Class A
    def m2(self):
        print("m2 is method of Derived or Sub or Child Class B..")   
b1 = B()   
b1.m1()   
b1.m2()

'''
OUTPUT:
m1 is method of Main or Base Class A..
m2 is method of Derived or Sub or Child Class B..
'''
