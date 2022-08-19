# Write  a program that uses the getpass module to prompt the user for a password, without echoing what they type to the console.
import getpass
password = getpass.getpass(prompt = 'Enter the password:')
if password == 'oxford':
    print('Welcome to the world of Python Programming!')
else:
    print('Incorrect password!')
'''
OUTPUT:
Enter the password:oxford
Welcome to the world of Python Programming!

Enter the password:python
Incorrect password!
'''
