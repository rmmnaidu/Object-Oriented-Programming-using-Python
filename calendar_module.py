# Write  a program to display a calendar of a given month
import calendar 
m = int(input('Enter month number:'))
y = int(input('Enter year:')) 
print(calendar.month(y,m))
'''
OUTPUT:
Enter month number:7
Enter year:2022
     July 2022
Mo Tu We Th Fr Sa Su
             1  2  3
 4  5  6  7  8  9 10
11 12 13 14 15 16 17
18 19 20 21 22 23 24
25 26 27 28 29 30 31
'''
