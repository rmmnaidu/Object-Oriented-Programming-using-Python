# Program to handle exceptions from an invoked function
def Divide(num, denom):
    try:
        quo = num/denom
        print("Quotient = :",quo)
    except ZeroDivisionError:
        print("You cannot divide a number by zero..Program terminating..")
Divide(20,0)
Divide(20,4)    
'''
OUTPUT:
Quotient = 2.857142857142857
You cannot divide a number by zero..Program Terminating..
'''
