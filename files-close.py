# Program to access a file after it is closed
fi = open("python.txt",mode="r")
print("Name of the file: ", fi.name)
print("Opening mode : ", fi.mode)
print("File is now being closed, You cannot use the file object fi:")
fi.close()
print("File is closed: ", fi.closed)
print("file is readable: ",fi.readable())
print("file is writable: ",fi.writable())

'''
OUTPUT:
Name of the file:  python.txt
Opening mode :  r
File is now being closed, You cannot use the file object fi:
File is closed:  True
Traceback (most recent call last):
  File "C:/Users/admin/Downloads/CBIT OOPS USING PYTHON w.e.f. 13.06.2022/files-close.py", line 8, in <module>
    print("file is readable: ",fi.readable())
ValueError: I/O operation on closed file
'''
