# Write a function to return more than one value 
def calculate(x,y): 
     return x+y, x-y, x*y, x/y 
a,b,c,d = calculate(10,20)
print("x+y = ",a) 
print("x-y = ",b) 
print("x*y = ",c) 
print("x/y = ",d)   
   
'''
OUTPUT:
x+y =  30
x-y =  -10
x*y =  200
x/y =  0.5
'''
