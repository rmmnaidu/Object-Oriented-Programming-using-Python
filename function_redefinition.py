# Program to demonstrate function redefinition
import datetime
def showmessage(msg):
    print(msg)
showmessage("Hello")
def showmessage(msg): # function redefinition
    now = datetime.datetime.now()
    print(msg)
    print(str(now))
showmessage("Current Date and Time is: ")
'''
OUTPUT:
Hello
Current Date and Time is: 
2022-07-03 13:28:53.838092
'''
