#Pgm 4.3 Write a program to determine whether a person is eligible to vote or not. If the person is not eligible, display how many years are left to eligible.
age = int(input("Enter the age:"))
if(age>=18):
    print("You are eligble to vote")
else:
    years = 18-age
    print("You have to wait for another " +str(years)+" years to cast your vote")

'''
Output:
Enter the age:18
You are eligble to vote
Enter the age:19
You are eligble to vote
Enter the age:17
You have to wait for another 1 years to cast your vote
Enter the age:12
You have to wait for another 6 years to cast your vote
'''
