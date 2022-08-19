# Program to calculate the factorial of a number recursively
def exp_rec(x, y):
    if(y == 0):
        return 1
    else:
        return (x*exp_rec(x, y-1))
n = int(input("Enter the first number:"))
m = int(input("Enter the second number:"))
print("Result = ", exp_rec(n, m))
'''
OUTPUT:
Enter the first number:2
Enter the second number:3
Result =  8
Enter the first number:3
Enter the second number:2
Result =  9
'''
