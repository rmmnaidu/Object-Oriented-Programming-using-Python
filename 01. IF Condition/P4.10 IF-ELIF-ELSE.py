#Pgm 4.10. Write a program to find the greatest number from three numbers
num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))
num3 = int(input("Enter third number:"))
if(num1>num2):
    if(num1>num3):
        print(num1," is greater than",num2,"and",num3)
    else:
        print(num3," is greater than",num1,"and",num2)      
elif(num2>num3):
    print(num2," is greater than",num1,"and",num3)
else:
    print("The three numbers are equal")

'''
Output:
Enter first number:50
Enter second number:40
Enter third number:30
50  is greater than 40 and 30
Enter first number:10
Enter second number:30
Enter third number:20
30  is greater than 10 and 20
Enter first number:10
Enter second number:20
Enter third number:30
The three numbers are equal
'''
