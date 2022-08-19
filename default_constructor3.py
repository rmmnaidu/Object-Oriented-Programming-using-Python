# Write a program to illustrate parameterized constructor
class users:
    name = ""
    def __init__(self, name):
        self.name = name
    def sayHello(self):
        print("Welcome to Python Developers, " + self.name) 
user1 = users("RAM")
user1.sayHello() 
  
'''
OUTPUT:
Welcome to Python Developers, RAM
'''
     
