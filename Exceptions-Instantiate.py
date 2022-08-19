# Program to understand the process of instantiating an exception
try:
    raise Exception("Hello", "World")
except Exception as errorObj:
    print(type(errorObj)) # the exception instance
    print(errorObj.args) # arguments stored in .args
    print(errorObj) # __str__() allows args to be printed directly
    arg1, arg2 = errorObj.args
    print("Argument1 = ", arg1)
    print("Argument2 = ", arg2)

'''
OUTPUT:
<class 'Exception'>
('Hello', 'World')
('Hello', 'World')
Argument1 =  Hello
Argument2 =  World
'''
