# Program to raise an exception with arguments
try:
    raise Exception("Hello", "World")
except ValueError:
    print("Program Terminating..")
    
'''
OUTPUT:
Traceback (most recent call last):
  File "F:/RMM OOPP UNIT-5/Exceptions-rasie with arguments.py", line 3, in <module>
    raise Exception("Hello", "World")
Exception: ('Hello', 'World')
'''
