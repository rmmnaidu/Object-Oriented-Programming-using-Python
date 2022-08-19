#Pgm 4.2 Write a program to determine the character entered by the user.
char = input("Enter any key from the keyboard:")
if(char.isalpha()):
    print("The user has entered a character")
if(char.isdigit()):
    print("The user has entered a digit")
if(char.isspace()):
    print("The user has entered a whitespace character")
'''
Output:
Enter any key from the keyboard:r
The user has entered a character
Enter any key from the keyboard:R
The user has entered a character
Enter any key from the keyboard:9
The user has entered a digit
Enter any key from the keyboard:HERE PRESS WHITE SPACE KEY 
The user has entered a whitespace character
'''
