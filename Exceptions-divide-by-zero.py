# Program to handle the divide by zero exception
num = int(input("Enter the numerator:"))
denom = int(input("Enter the denominator:"))
try:
    quo = num/denom
    print("Quotient:",quo)
except ZeroDivisionError:
    print("Denominator cannot be zero..")
'''
OUTPUT:
Enter the numerator:20
Enter the denominator:10
Quotient: 2.0
-------------------------
Enter the numerator:30
Enter the denominator:0
Denominator cannot be zero..

'''
