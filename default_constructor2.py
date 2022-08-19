# Write a program to count no. of objects created for a class 
class test:
    count = 0
    def __init__(self):
        test.count = test.count + 1
    def display():
        print('No. of objects = ',test.count)
t1=test()
t2=test() 
t3=test() 
t4=test() 
t5=test() 
t6=test() 
test.display()   
  
'''
OUTPUT:
No. of objects =  6
'''
     
