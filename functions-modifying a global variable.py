#Program to demonstrate access of variables in inner and outer functions 
def outer_func():
    outer_var = 20
    def inner_func():
        inner_var = 30
        print("Outer variable = ",outer_var)
        print("Inner variable = ",inner_var)
    inner_func()
    print("Outer variable = ",outer_var)
    print("Inner variable = ",inner_var)#Not accessible
outer_func() #Function call
'''
Output:
Outer variable =  20
Inner variable =  30
Outer variable =  20
Traceback (most recent call last):
  File "C:/Users/admin/Downloads/CBIT OOPS USING PYTHON w.e.f. 13.06.2022/RMM OOPP LAB PROGRAMS/functions-modifying a global variable.py", line 11, in <module>
    outer_func() #Function call
  File "C:/Users/admin/Downloads/CBIT OOPS USING PYTHON w.e.f. 13.06.2022/RMM OOPP LAB PROGRAMS/functions-modifying a global variable.py", line 10, in outer_func
    print("Inner variable = ",inner_var)#Not accessible
NameError: name 'inner_var' is not defined
'''
