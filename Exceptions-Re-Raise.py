# Program to re-raise an exception
try:
    raise NameError
except:
    print("Re-Raising the Exception..")
    raise

'''
OUTPUT:
10
Exception occurred...Program Terminating..
'''
