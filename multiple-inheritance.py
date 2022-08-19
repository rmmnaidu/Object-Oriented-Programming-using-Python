# Program to implement multiple inheritance
class Calculation1:
    def Addition(self,a,b):
        return a+b
class Calculation2:
    def Multiplication(self,a,b):
        return a*b
class Calculation3:
    def Divison(self,a,b):
        return a/b
class Derived(Calculation1,Calculation2,Calculation3): #derived class from 3 base classes
    def Mod(self,a,b):
        return a%b
d = Derived()   
print("Addition:",d.Addition(10,20))
print("Multiplication:",d.Multiplication(10,5))
print("Divison:",d.Divison(20,10))
print("Modulo Divison:",d.Mod(40,15)) 

'''
OUTPUT:
Addition: 30
Multiplication: 50
Divison: 2.0
Modulo Divison: 10
'''
