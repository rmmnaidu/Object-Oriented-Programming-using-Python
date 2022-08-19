# Program that demonstrates using a local variable with same name as that of global 
def f():
    print(str) # global
    str = "Helo World!" # local
    print(str)
str = "Welcome to Object Oriented Programming using Python" 
f()
    
'''
OUTPUT:
UnboundLocalError: local variable 'str' referenced before assignment
'''
