#Program 4.50 Write a program to print the followig pattern
'''
0
12
345
6789
'''
count = 0
for i in range(1,5):
    print() #prints a new line
    for j in range(1,i+1):
        print(count, end='')
        count = count+1
    
    
