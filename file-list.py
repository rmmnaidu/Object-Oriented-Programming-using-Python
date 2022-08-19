# Program to display the contents of the file write.txt using the list() method
f = open("write.txt","r")
print(list(f)) 
f.close() 

'''
OUTPUT:
['Python is dynamic programming language\n', 'C is a structured programming language\n', 'Java is an object oriented programming language\n', 'Welcome to the course\n', 'Python programming\n', 'for every beginners..']
'''
