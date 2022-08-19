# Positional as well as keyword arguments
def print_it(i, a, str):
    print(i, a, str)
print_it(10, a = 3.14, str = 'Python') # ok
print_it(10, str = 'Python', a = 3.14) # ok
print_it(str = 'Python',10, a = 3.14) # error, positional after keyword
print_it(str = 'Python',a = 3.14, 10) # error, positional after keyword

'''
OUTPUT:
Syntax Error:
Positional argument follows keyword arguments
'''
