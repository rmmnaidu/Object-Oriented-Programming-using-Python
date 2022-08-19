# Program to open a file and check the list of attributes
fi = open("python.txt",mode="r")
print("Name of the file: ", fi.name)
print("Closed or not : ", fi.closed)
print("Opening mode : ", fi.mode)
print("file is readable: ",fi.readable())
print("file is writable: ",fi.writable())

'''
OUTPUT:
Name of the file:  python.txt
Closed or not :  False
Opening mode :  r
file is readable:  True
file is writeable:  False
'''
