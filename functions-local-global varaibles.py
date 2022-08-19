#Program to understand the difference between local and global variables
num1 = 20 # global variable
print("Global variable num1 = ",num1)
def func(num2): #num2 is a function parameter
    print("In Function - Local Variable num2 = ",num2)
    num3 = 30 # num3 is a local variable
    print("In Function - Local Variable num3 = ",num3)
func(40) # 40 is passed as an argument i.e. num2 to the function
print("num1 again = ",num1) # global variable is being accessed
print("num3 outside function = ",num3)# Error-Local variable can't be used outside the function in which it is defined

'''
Output:
Global variable num1 =  20
In Function - Local Variable num2 =  40
In Function - Local Variable num3 =  30
num1 again =  20
Traceback (most recent call last):
  File "C:/Users/admin/Downloads/CBIT OOPS USING PYTHON w.e.f. 13.06.2022/RMM OOPP LAB PROGRAMS/functions-local-global varaibles.py", line 10, in <module>
    print("num3 outside function = ",num3)# Error-Local variable can't be used outside the function in which it is defined
NameError: name 'num3' is not defined. Did you mean: 'num1'?
'''
