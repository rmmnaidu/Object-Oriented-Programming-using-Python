# Program to To read only first 20 characters from the file write.txt
f = open("write.txt","r")
data = f.read(20)
print("First 20 characters from the file write.txt is..\n", data) 
f.close()

'''
OUTPUT:
First 20 characters from the file write.txt is..
 Python is dynamic pr
'''
