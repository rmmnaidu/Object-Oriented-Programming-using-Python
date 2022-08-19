# Program to append data to already existing file write.txt
f = open("write.txt","a")
f.write("Welcome to the course\n")
f.write("Python programming\n")
f.write("for every beginners..")
print("Data written to the file successfully!") 
f.close()

'''
OUTPUT:
Data written to the file successfully!

write.txt before append:
-----------------------
Python is dynamic programming language
C is a structured programming language
Java is an object oriented programming language

write.txt after append:
-----------------------
Python is dynamic programming language
C is a structured programming language
Java is an object oriented programming language
Welcome to the course
Python programming
for every beginners..
'''
