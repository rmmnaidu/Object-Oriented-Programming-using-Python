#Pgm 4.4 Write a program to find larger of two numbers
a = int(input("Enter the value of a:"))
b = int(input("Enter the value of b:"))
if(a>b):
    large = a
else:
    large = b
print("Larger number = ",large)

'''
Output:
Enter the value of a:20
Enter the value of b:10
Larger number =  20
Enter the value of a:30
Enter the value of b:40
Larger number =  40
'''
