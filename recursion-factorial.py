# Program to calculate the factorial of a number recursively
def fact(n):
    if(n == 1 or n == 0):
        return 1
    else:
        return n * fact(n-1)
n = int(input("Enter the value of n:"))
print("The factorial of", n, "is", fact(n))
'''
OUTPUT:
Enter the value of n:3
The factorial of 3 is 6
Enter the value of n:5
The factorial of 5 is 120
'''
