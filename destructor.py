# Program to demonstrate destructor  
class employee:
    def __init__(self):
        print('Employee created..')
    def __del__(self):
        print('Destructor called,Employee  deleted..')    
e1 = employee() 
del e1   

'''
OUTPUT:
Employee created..
Destructor called,Employee  deleted..
'''
