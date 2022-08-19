# Program to overload hex(), oct(), and float() functions
class Number:
    def __init__(self, num):
        self.num = num
    def display(self):
        return self.num
    def __abs__(self):
        return abs(self.num)
    def __float__(self):
        return float(self.num)
    def __oct__(self):
        return oct(self.num)
    def __hex__(self):
        return hex(self.num)
    def __setitem__(self, num):
        self.num = num
N = Number(-12)
print("N is:", N.display())
print("ABS(N)is:", abs(N))
N = abs(N)
print("Converting to FLOAT..., N is:", float(N))
print("HEXADECIAML equivalent of N is:", hex(N))
print("OCTAL equivalent of N is:", oct(N))

'''
OUTPUT:
N is: -12
ABS(N)is: 12
Converting to FLOAT..., N is: 12.0
HEXADECIAML equivalent of N is: 0xc
OCTAL equivalent of N is: 0o14
'''

        
       
