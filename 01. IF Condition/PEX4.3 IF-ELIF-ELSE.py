#Example 4.3. Write a program to test whether a number entered by the user is negative, positive, or equal to zero.
num = int(input("Enter any number:"))
if(num==0):
    print("The value is equal to zero")
elif(num>0):
    print("The number is positive")
else:
    print("The number is negative")

'''
Output:
Enter any number:0
The value is equal to zero
Enter any number:1
The number is positive
Enter any number:-4
The number is negative
'''
