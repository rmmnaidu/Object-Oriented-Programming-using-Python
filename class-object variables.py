# Program to differentiate between class and object variables 
class test:
    class_var = 0 # class variable
    def __init__(self, var):
        test.class_var+= 1
        self.var = var # object variable
        print("The object value is: ", var)
        print("The value of class variable is: ", test.class_var)    
obj1 = test(10)
obj2 = test(20)
obj3 = test(30)
   
'''
OUTPUT:
The object value is:  10
The value of class variable is:  1
The object value is:  20
The value of class variable is:  2
The object value is:  30
The value of class variable is:  3
'''
