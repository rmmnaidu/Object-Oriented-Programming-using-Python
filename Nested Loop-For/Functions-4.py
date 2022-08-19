# write a function to find the biggest of two numbers  
def biggest(x,y):
    if x>y:
        return x
    else:
        return y
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
big = biggest(a,b)
print('Biggest number =',big) 
'''
OUTPUT:
Enter first number20
Enter second number10
Biggest number = 20
Enter first number:20
Enter second number:30
Biggest number = 30
'''
