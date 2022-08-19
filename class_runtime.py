# Program to add variables to a class at run-time
class test():
    def __init__(self, var):
        self.var = var
    def display(self):
        print("Var is = ", self.var)       
obj = test(10)
obj.display()
obj.new_var = 20 # variable added at run-time
print("New Var = ", obj.new_var)
obj.new_var = 30 # modifying newly added variable
print("New Var after modification = ", obj.new_var)
del obj.new_var # newly created variable is deleted
print("New Var after deletion = ", obj.new_var)
'''
OUTPUT:
Var is =  10
New Var =  20
New Var after modification =  30
Traceback (most recent call last):
  File "C:/Users/admin/Downloads/CBIT OOPS USING PYTHON w.e.f. 13.06.2022/RMM OOPP LAB PROGRAMS/class_runtime.py", line 14, in <module>
    print("New Var after deletion = ", obj.new_var)
AttributeError: 'test' object has no attribute 'new_var'
'''
