# Write a program that prints absolute value, square root, and cube of a number 
import math

def cube(x):
    return x**3

a = -25
print("a = ",a)
a = abs(a)
print("abs(a) = ",a)
print("Square root of ",a, " = ",math.sqrt(a))
print("Cube of ",a, " = ",cube(a))

'''
OUTPUT:
a =  -25
abs(a) =  25
Square root of  25  =  5.0
Cube of  25  =  15625
'''
