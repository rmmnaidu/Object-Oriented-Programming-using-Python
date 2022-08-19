#Pgm 4.8 Write a program to find whether a given year is a leap year or not. 
year = int(input("Enter any year:"))
if((year%4==0 and year%100!=0) or (year%400==0)):
    print("Leap Year!")
else:
    print("Not a Leap Year!")

'''
Output:
Enter any year:2016
Leap Year!
Enter any year:2020
Leap Year!
Enter any year:2021
Not a Leap Year!
Enter any year:2022
Not a Leap Year!
Enter any year:2024
Leap Year!
'''
