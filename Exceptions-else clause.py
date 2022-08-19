# Program to demonstrate else block.
try:
    f1 = open('File1.txt') 
    str1 = f1.readline()
    print(str1)
except IOError:
    print("Error occured during Input...Program Terminated..")
except:
    print("Error occured..Program Terminated..")
else:
    print("Program Terminated successfully..")

'''
OUTPUT:
By including f1 = open('File1.txt') 
Welcome to the course

Program Terminated successfully..

'''
