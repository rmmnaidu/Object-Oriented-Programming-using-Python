#Pgm 4.14 Write a program to calculate students marks total, average and display the grade obtained by the student.
marks1 = int(input("Enter the marks in Mathematics:"))
marks2 = int(input("Enter the marks in English:"))
marks3 = int(input("Enter the marks in C Programming:"))
marks4 = int(input("Enter the marks in Drawing:"))
total = marks1+marks2+marks3+marks4
avg = float(total)/4
print("Total = ",total,"\t Aggragate = ",avg)
if(avg>=75):
    print("Distinction")
elif(avg>=60 and avg<75):
    print("First Division")
elif(avg>=50 and avg<60):
    print("Second Division")
elif(avg>=40 and avg<50):
    print("Third Division")
else:
    print("Fail!")          
        
 
'''
Output:
Enter the marks in Mathematics:50
Enter the marks in English:60
Enter the marks in C Programming:80
Enter the marks in Drawing:60
Total =  250 	 Aggragate =  62.5
First Division
Enter the marks in Mathematics:80
Enter the marks in English:90
Enter the marks in C Programming:90
Enter the marks in Drawing:80
Total =  340 	 Aggragate =  85.0
Distinction
'''
