num = int(input("Enter any number:"))
fact = 1
for i in range(1,num + 1):
    fact = fact * i
print("The factorial of %d = %d"%(num, fact))
