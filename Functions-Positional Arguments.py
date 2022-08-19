def fun(i, j, k):
    print(i + j)
    print(k.upper( ))
fun(10, 20.0, 'Python') # correct call
fun('Python', 20.0, 10) # error, incorrect order
'''
OUTPUT:
30.0
PYTHON
Traceback (most recent call last):
  File "C:/Users/admin/Downloads/CBIT OOPS USING PYTHON w.e.f. 13.06.2022/RMM OOPP LAB PROGRAMS/Functions-Positional Arguments.py", line 5, in <module>
    fun('Python', 20.0, 10) # error, incorrect order
  File "C:/Users/admin/Downloads/CBIT OOPS USING PYTHON w.e.f. 13.06.2022/RMM OOPP LAB PROGRAMS/Functions-Positional Arguments.py", line 2, in fun
    print(i + j)
TypeError: can only concatenate str (not "float") to str
'''
