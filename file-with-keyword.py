# Program to use with keyword for opening a file write.txt
with open("write.txt","w") as f:
    f.write("AIDS-2\n")
    f.write("B.E II Semester")
print("Name of the File opened: ",f.name)
print("Is File Closed: ",f.closed)# by default file is closed by using with keyword
print("File Mode: ",f.mode)

'''
OUTPUT:
Name of the File opened:  write.txt
Is File Closed:  True
File Mode:  w
'''
