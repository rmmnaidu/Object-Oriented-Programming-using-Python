# Write a function to return only one value 
def biggest(x, y):
    if x>y:
        return x
    else:
        return y
print("Biggest Number = ",biggest(10, 20))
print("Biggest Number = ",biggest(100, 20))
print("Biggest Number = ",biggest(20, 40))    
'''
OUTPUT:
Biggest Number =  20
Biggest Number =  100
Biggest Number =  40
'''
