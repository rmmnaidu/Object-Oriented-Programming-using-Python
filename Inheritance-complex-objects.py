# Program that uses complex objects
class one:
    def set(self, var):
        self.var = var
    def get(self):
        return self.var
class two:
    def __init__(self, var):
        self.o = one() # object of class one is created
        # method of Class one is invoked using its object in Class two
        self.o.set(var)
    def show(self):
        print("Number = ",self.o.get())
t = two(300)
t.show()

'''
OUTPUT:
Number =  300
'''
