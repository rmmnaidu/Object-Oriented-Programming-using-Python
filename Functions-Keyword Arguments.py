# Keyword arguments
def print_it(i, a, str):
    print(i, a, str)
print_it(a = 3.14, i = 10, str = 'Python') # keyword, ok
print_it(str = 'Python',a = 3.14, i = 10) # keyword, ok
print_it(str = 'Python',i = 10, a = 3.14) # keyword, ok
print_it(s = 'Python',j = 10, a = 3.14) # keyword, keyword name

'''
OUTPUT:
10 3.14 Python
10 3.14 Python
10 3.14 Python
Traceback (most recent call last):
  File "C:/Users/admin/Downloads/CBIT OOPS USING PYTHON w.e.f. 13.06.2022/RMM OOPP LAB PROGRAMS/Functions-Keyword Arguments.py", line 7, in <module>
    print_it(s = 'Python',j = 10, a = 3.14) # keyword, keyword name
TypeError: print_it() got an unexpected keyword argument 's'
'''
