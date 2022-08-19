# Program to demonstrate the use of except: block
try:
    #f1 = open('File1.txt','r') 
    str1 = f1.readlines()
    print(str1)
except IOError:
    print("Error occured during Input...Program Terminated..")
except ValueError:
    print("Could not convert data to an integer..")
except:
    print("Unexpected Error..Program Terminating..")

'''
OUTPUT:
By including f1 = open('File1.txt','r') 
['Welcome to the course\n', 'Object Oriented Porgramming using Python']
By excluding #f1 = open('File1.txt','r') 
Unexpected Error..Program Terminating..
'''
