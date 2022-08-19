# Write a program to illustrate parameterized constructor
class car:
    def __init__(self,x,y,z):
        self.color = x
        self.companyname = y
        self.model = z     
    def display(self):
        print('Car color: ',self.color)
        print('Car company name: ',self.companyname)
        print('Car model name: ',self.model) 
c1 = car('Red','KIA','SELTOS') 
c1.display()   
'''
OUTPUT:
Car color:  Red
Car company name:  KIA
Car model name:  SELTOS
'''
     
