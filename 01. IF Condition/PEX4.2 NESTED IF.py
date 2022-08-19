#Example 4.2. Write a program that prompts the user to enter and then print its interval
num = int(input("Enter any number from 0-30:"))
if(num>=0 and num<10):
    print("It is in the range 0-10")
if(num>=10 and num<20):
    print("It is in the range 10-20")
if(num>=20 and num<30):
    print("It is in the range 20-30")

'''
Output:
Enter any number from 0-30:2
It is in the range 0-10
Enter any number from 0-30:10
It is in the range 10-20
Enter any number from 0-30:25
It is in the range 20-30
'''
