# Program to demonstrate readline() method from the file write.txt
f = open("write.txt","r")
line1 = f.readline() 
print(line1,end='') 
line2=f.readline() 
print(line2,end='') 
line3=f.readline() 
print(line3,end='') 
f.close() 

'''
OUTPUT:
Python is dynamic programming language
C is a structured programming language
Java is an object oriented programming language
'''
