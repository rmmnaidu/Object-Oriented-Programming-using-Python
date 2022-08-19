# Program to illustrate the use of special methods in Python classes
class test():
    def __init__(self, name, var):
        self.name = name
        self.var = var
    def __repr__(self):
        return repr(self.var)
    def __len__(self):
        return len(self.name)
    def __cmp__(self, obj):
        return self.var - obj.var
obj = test("pythoncourse", 10)
print("The value stored in object is:", repr(obj))
print("The length of name stored in object is:", len(obj))
obj1 = test("oopup", 1)
val = obj.__cmp__(obj1)
if val == 0:
    print("Both are equal..")
elif val == -1:
    print("First value is less than second..")
else:
    print("Second value is less than first..")
    
'''
OUTPUT:
The value stroed in object is: 10
The length of name stored in object is: 12
Second value is less than first..
'''
