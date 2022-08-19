# Variable length arugments
def print_it(*args):
    print()
    for var in args:
        print(var, end=' ')
print_it(10) # 1 arg, ok
print_it(10, 3.14) # 2 args, ok
print_it(10, 3.14, 'Python') # 3 args, ok
print_it(10, 3.14, 'Python', 'Version 3.10.4') # 4 args, ok


'''
OUTPUT:
10 
10 3.14 
10 3.14 Python 
10 3.14 Python Version 3.10.4 
'''
