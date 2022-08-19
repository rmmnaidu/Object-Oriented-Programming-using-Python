# Program to perform split operation whenever a comma (,) is encountered in the file writelines1.txt
with open("writelines1.txt","r") as f:
    line = f.readline()
    words = line.split(',') # Splits based on comma (,)
    print(words)
    
'''
writelines1.txt:
---------------
Welcome to the course, Python programming, for every beginners.

Output:
------
['Welcome to the course', ' Python programming', ' for every beginners.']
'''
