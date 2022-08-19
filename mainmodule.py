# mainmodule.py
import MyModule
print("MyModule str = ",MyModule.str) # using variable defined in MyModule
MyModule.display() # using the function defined in MyModule
print("Name of calling module is:",__name__)

'''
OUTPUT:
MyModule str =  Welcome to course Python!
Hello
Name of called module is: MyModule
Name of calling module is: __main__
'''
