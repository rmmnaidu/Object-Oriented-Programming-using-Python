# Program to print the Fibonacci series using recursion.
def fibonacci(n):
    if(n<2):
        return 1
    else:
        return (fibonacci(n-1)+ fibonacci(n-2))
n = int(input("Enter the number of terms:"))
for i in range(n):
    print("Fibonacci(",i,") = ", fibonacci(i))
'''
OUTPUT:
Enter the number of terms:5
Fibonacci( 0 ) =  1
Fibonacci( 1 ) =  1
Fibonacci( 2 ) =  2
Fibonacci( 3 ) =  3
Fibonacci( 4 ) =  5
'''
