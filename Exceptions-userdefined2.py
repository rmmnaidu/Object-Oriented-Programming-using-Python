# Program to create sub-classes for Exception class to handle exceptions in a better customized way
class Error(Exception):
    def message(self):
        raise NotImplementedError()
class InputError(Error):
    def __init__(self, expr, msg):
        self.expr = expr
        self.msg = msg
    def message(self):
        print("Error in input in Expression..")
        print(self.expr)
try:
    a = input("Enter the value of a:")
    raise InputError("input(\"Enter the value of a:s\")","Input Error")
except InputError as ie:
    ie.message()

'''
OUTPUT:
Enter the value of a:20
Error in input in Expression..
input("Enter the value of a:s")
'''
