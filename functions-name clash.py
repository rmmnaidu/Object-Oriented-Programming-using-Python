# Program to demonstrate name clash variables in case of nested functions
def outer_func():
    var = 20
    def inner_func():
        var = 30
        print("Inner variable = ",var)
    inner_func()
    print("Outer variable = ",var)
outer_func() #Function call
'''
OUTPUT:
Inner variable =  30
Outer variable =  20
'''
