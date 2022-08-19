# Program to define a user-defined exception
class myError(Exception):
    def __init__(self, val):
        self.val = val
    def __str__(self):
        return repr(self.val)
try:
    raise myError(30)
except myError as e:
    print("User-defined Exception Generated with value: ",e.val)

'''
OUTPUT:
User-defined Exception Generated with value:  30
'''
