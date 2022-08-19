# Program to implement hierarchical inheritance
class A: # Base class
    def m1(self):
        print("I am m1 of Base Class A!")
class B(A): # Derived Class1 from Base Class A
    def m2(self):
        print("I am m2 of Derived Class B!")
class C(A): # Derived Class2 from Base Class A
    def m3(self):
        print("I am m3 of Derived Class C!")
class D(A): # Derived Class3 from Base Class A
    def m4(self):
        print("I am m4 of Derived Class D!")
b1 = B()
b1.m1() # derived from Base Class A
b1.m2() # Own method of Class B
c1 = C()
c1.m1() # derived from Base Class A
c1.m3() # Own method of Class C
d1 = D()
d1.m1() # derived from Base Class A
d1.m4() # Own method of Class D
'''
OUTPUT:
I am m1 of Base Class A!
I am m2 of Derived Class B!
I am m1 of Base Class A!
I am m3 of Derived Class C!
I am m1 of Base Class A!
I am m4 of Derived Class D!
'''

