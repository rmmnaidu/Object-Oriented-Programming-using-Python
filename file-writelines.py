# Program that writes a message into the file, writelines.txt
f = open("writelines.txt","w")
lines = ["Welcome to the course\n","Python programming\n","for every beginners.."]
f.writelines(lines) 
print("Data written to the file successfully!") 
f.close()
'''
OUTPUT:
Data written to the file successfully!

Open the file writelines.txt:
Welcome to the course
Python programming
for every beginners..

'''
