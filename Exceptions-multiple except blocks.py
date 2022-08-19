# Program with multiple except block
try:
    num = int(input("Enter the number:"))
    print(num**2)
except (KeyboardInterrupt):
    print("You shoud have entered a command from keyboard....Program Terminating..")
except (ValueError):
    print("Please check before you enter...Program Terminating..")
print("Bye..")

'''
OUTPUT:
Enter the number:10
100
Bye..

Enter the number:"Hi"
Please check before you enter...Program Terminating..
Bye..

Enter the number:abc
Please check before you enter...Program Terminating..
Bye..

Enter the number:!
Please check before you enter...Program Terminating..
Bye..

Enter the number: PRESS CTRL+C Command
You shoud have entered a command from keyboard....Program Terminating..
Bye..
'''
