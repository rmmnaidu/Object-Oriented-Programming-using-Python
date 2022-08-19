#Pgm 4.7 Write a program to calculate the bonus of employee of a company. 5% bonus for male and 10% bonus for female. 
ch = input("Enter gender of employee male-m or female-f:")
sal = int(input("Enter the salary of the employee:"))
if(ch=='m'):
    bonus = 0.05*sal
else:
    bonus = 0.10*sal
amount_to_be_paid = sal+bonus
print("Salary = ",sal)
print("Bonus = ",bonus)
print("---------------------------------------------")
print("Total Amount to be paid: ",amount_to_be_paid)

'''
Output:
Enter gender of employee male-m or female-f:m
Enter the salary of the employee:20000
Salary =  20000
Bonus =  1000.0
---------------------------------------------
Total Amount to be paid:  21000.0

Enter gender of employee male-m or female-f:f
Enter the salary of the employee:15000
Salary =  15000
Bonus =  1500.0
---------------------------------------------
Total Amount to be paid:  16500.0
'''
