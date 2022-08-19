# Program illustrating the modification of an instance variable
class Number:
    even = 0 # default value
    def check(self, num):
        if num%2 == 0:
            self.even = 1
    def Even_Odd(self, num):
        self.check(num)
        if self.even == 1:
            print(num, "is even")
        else:
            print(num, "is odd")
n = Number()
n.Even_Odd(21)

'''
OUTPUT:
21 is odd
'''
