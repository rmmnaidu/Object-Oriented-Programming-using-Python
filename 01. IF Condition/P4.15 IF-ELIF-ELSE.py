#Pgm 4.15 Write a program to calculate roots of a quadratic equation.
a = int(input("Enter the value of a:"))
b = int(input("Enter the value of b:"))
c = int(input("Enter the value of c:"))
D = (b*b)-(4*a*c)
denom = 2*a
if(D>0):
    print("Real Roots...")
    root1 = (-b+D**0.5)/denom
    root2 = (-b-D**0.5)/denom
    print("Root1 = ",root1,"\t Root2 = ",root2)
elif(D==0):
    print("Equal Roots...")
    root1 = -b/denom
    print("Root1 and Root2 = ",root1)
else:
    print("Imaginary Roots...")


'''
Output:
Enter the value of a:1
Enter the value of b:-6
Enter the value of c:8
Real Roots...
Root1 =  4.0 	 Root2 =  2.0
Enter the value of a:1
Enter the value of b:2
Enter the value of c:3
Imaginary Roots...
Enter the value of a:4
Enter the value of b:4
Enter the value of c:1
Equal Roots...
Root1 and Root2 =  -0.5
'''
