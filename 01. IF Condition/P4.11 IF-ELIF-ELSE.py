#Pgm 4.11. Write a program that prompts the user to enter a number between 1-7 and then displays the corresponding day of the week
num = int(input("Enter any number between 1 to 7:"))
if(num==1):
    print("Sunday")
elif(num==2):
    print("Monday")
elif(num==3):
    print("Tuesday")
elif(num==4):
    print("Wednesday")
elif(num==5):
    print("Thursday")
elif(num==6):
    print("Friday")
elif(num==7):
    print("Saturday")
else:
    print("Wrong input")

'''
Output:
Enter any number between 1 to 7:1
Sunday
Enter any number between 1 to 7:2
Monday
Enter any number between 1 to 7:3
Tuesday
Enter any number between 1 to 7:4
Wednesday
Enter any number between 1 to 7:5
Thursday
Enter any number between 1 to 7:6
Friday
Enter any number between 1 to 7:7
Saturday
Enter any number between 1 to 7:8
Wrong input
'''
