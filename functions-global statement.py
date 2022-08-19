#Program to demonstrate the use of global statement
var = "Good" # global variable
def show(): 
    global var1
    var1 = "Morning"
    print("In Function var is:",var)
show()
print("Outside function, var1 is:",var1)# Accessible as it is global variable
print("Var is:",var)
'''
Output:
In Function var is: Good
Outside function, var1 is: Morning
Var is: Good
'''
