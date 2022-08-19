#Pgm 4.12. Write a program to calculate the tax for the given conditions:
'''
If Income is <1.5L then no tax
If Income is between 1,50,001 to 3L then charge 10% of tax
If Income is between 3,00,001 to 5L then charge 20% of tax
If Income is > 5,00,001 then charge 30% of tax
'''
MIN1 = 150001
MAX1 = 300000
RATE1 = 0.10
MIN2 = 300001
MAX2 = 500000
RATE2 = 0.20
MIN3 = 500001
RATE3 = 0.30
income = int(input("Enter the income:"))
taxable_income = income - 150000
if(taxable_income<=0):
    tax = 0
    print("No Tax")
elif(taxable_income>=MIN1 and taxable_income<MAX1):
    tax = (taxable_income - MIN1) * RATE1
elif(taxable_income>=MIN2 and taxable_income<MAX2):
    tax = (taxable_income - MIN2) * RATE2
else:
    tax = (taxable_income - MIN3) * RATE3
print("TAX = ",tax)

'''
Output:
Enter the income:149000
No Tax
TAX =  0
Enter the income:600000
TAX =  29999.800000000003
Enter the income:1650000
TAX =  299999.7
'''
