# Program to handle exceptions in the calling function
def Divide(num, denom):
    quo = num/denom
    print("Quotient =",quo)      
try:
    Divide(20, 7)
    Divide(20, 0)
except ZeroDivisionError:
    print("You cannot divide a number by zero..Program Terminating..")

'''
OUTPUT:
You cannot divide a number by zero..Program Terminating..
'''
