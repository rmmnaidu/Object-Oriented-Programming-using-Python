# Program to split the line into a series of words and use space to perform the split operation in the file writelines.txt
with open("writelines.txt","r") as f:
    line = f.readline()
    words = line.split() # Splits based on space
    print(words)
    
'''
OUTPUT:
writelines.txt:
---------------
Welcome to the course
Python programming
for every beginners..
Output:
------
['Welcome', 'to', 'the', 'course']
'''
