# Program illustrating the use of __init()__ method
class test:
    def __init__(self,val): 
        print("In class method!")
        self.val = val
        print("The value is:", val)
obj = test(20)
  
'''
OUTPUT:
In class method!
The value is: 20
'''
