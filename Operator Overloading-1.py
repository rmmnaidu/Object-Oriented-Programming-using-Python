# Program to add two complex numbers without overloading the + operator
class Complex:
    def __init__(self):
        self.real = 0
        self.imag = 0
    def setValue(self, real, imag):
        self.real = real
        self.imag = imag
    def display(self):
        print("(", self.real, "+", self.imag, "i)")
C1 = Complex()
C1.setValue(1, 2)
C2 = Complex()
C2.setValue(3, 4)
C3 = Complex()
C3 = C1 + C2
C3.display()

'''
OUTPUT:
Traceback (most recent call last):
  File "C:/Users/admin/Downloads/CBIT OOPS USING PYTHON w.e.f. 13.06.2022/RMM OOPP LAB PROGRAMS/Operator Overloading-1.py", line 16, in <module>
    C3 = C1 + C2
TypeError: unsupported operand type(s) for +: 'Complex' and 'Complex'
'''

