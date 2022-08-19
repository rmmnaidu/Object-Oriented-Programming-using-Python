# Keyword Variable-Length Arguments
def print_it(**kwargs):
    print()
    for name, value in kwargs.items():
        print(name, value, end = ' ')
print_it(a = 10)#keyword, ok
print_it(a = 10, b = 3.14) #keyword, ok
print_it(a = 10, b = 3.14, s = 'Python') #keyword, ok
dct = {'Student':'rmm', 'Age':23}
print_it(**dct) #ok
'''
OUTPUT:
a 10 
a 10 b 3.14 
a 10 b 3.14 s Python 
Student rmm Age 23 
'''
