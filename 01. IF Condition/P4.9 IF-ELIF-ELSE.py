#Pgm 4.9. Write a program to demonstrate whether the character entered is a vowel or not.
ch = input("Enter any character:")
if(ch=="A" or ch=="E" or ch=="I" or ch=="O" or ch=="U"):
    print(ch," is a vowel")
elif(ch=="a" or ch=="e" or ch=="i" or ch=="o" or ch=="u"):
    print(ch," is a vowel")
else:
    print(ch," is not a vowel")

'''
Output:
Enter any character:A
A  is a vowel
Enter any character:a
a  is a vowel
Enter any character:B
B  is not a vowel
Enter any character:b
b  is not a vowel
Enter any character:u
u  is a vowel
Enter any character:U
U  is a vowel
'''
