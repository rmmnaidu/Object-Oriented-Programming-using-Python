#Program 4.51 Write a program to print the followig pattern
'''
    1
   12
  123
 1234
12345
'''
n = 5
for i in range(1,n+1):
    for k in range(n,i,-1):
        print(" ",end='')
    for j in range(1,i+1):
        print(j,end='')
    print() #prints a new line
    
    
