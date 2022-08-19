# Program having an except clause handling multiple exceptions simultaneously.
try:
    num = int(input("Enter the number:"))
    print(num**2)
except (KeyboardInterrupt, ValueError, TypeError):
     print("Please check before you enter...Program Terminating..")
print("Bye..")

'''
OUTPUT:
Enter the number:10
100
Bye..

Enter the number:abc
Please check before you enter...Program Terminating..
Bye..

Enter the number:PRESS CTRL+C Command
Please check before you enter...Program Terminating..
Bye..
'''
