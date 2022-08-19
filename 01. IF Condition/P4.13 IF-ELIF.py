#Pgm 4.13 Write a program to take input from user and then check whether it is a number or a character. If it is a character, determine whether it is in uppercase or lowercase.
ch = input("Enter any character:")
if(ch>="A" and ch<="Z"):
    print("The UPPERCASE character was entered")
elif(ch>='a' and ch<='z'):
    print("The LOWERCASE character was entered")
elif(ch>='0' and ch<='9'):
    print("A NUMBER was entered")
    
'''
Output:
Enter any character:R
The UPPERCASE character was entered
Enter any character:r
The LOWERCASE character was entered
Enter any character:9
A NUMBER was entered
'''
