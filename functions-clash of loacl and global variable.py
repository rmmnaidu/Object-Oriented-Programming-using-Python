#Program to demonstrate the clash of local and global variable
var = "Good" # global variable
def show(): 
    var = "Morning"
    print("In Function var is:",var)
show()
print("Outside function, var is:",var)
'''
Output:
In Function var is: Morning
Outside function, var is: Good
'''
