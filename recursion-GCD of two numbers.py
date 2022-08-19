# Program to calculate the factorial of a number recursively
def GCD(x, y):
    rem = x%y
    if(rem == 0):
        return y
    else:
        return GCD(y, rem)
n = int(input("Enter the first number:"))
m = int(input("Enter the second number:"))
print("The GCD of numbers is", GCD(n, m))
'''
OUTPUT:
Enter the first number:50
Enter the second number:5
The GCD of numbers is 5
Enter the first number:10
Enter the second number:20
The GCD of numbers is 10
'''
