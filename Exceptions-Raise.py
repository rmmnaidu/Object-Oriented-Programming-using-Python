# Program to deliberately raise an exception
try:
    num = 10
    print(num)
    raise ValueError
except:
    print("Exception occurred...Program Terminating..")

'''
OUTPUT:
10
Exception occurred...Program Terminating..
'''
