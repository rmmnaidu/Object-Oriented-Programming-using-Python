# Program illustrating the use of __init()__ method
class person:
    def __init__(self,name): 
        print("In class method!")
        self.name = name
    def display(self):
        print("Hello", self.name)
        return
p1 = person('Ram')
p1.display()
  
'''
OUTPUT:
In class method!
Hello Ram
'''
