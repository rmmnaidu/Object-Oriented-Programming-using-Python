# Write a program to find given word is keyword or not. 
import keyword 
w = input("Enter any word:") 
if keyword.iskeyword(w):
    print("Given word is keyword") 
else:
    print("Given word is not a keyword") 
'''
OUTPUT:
Enter any word:if
Given word is keyword
Enter any word:int
Given word is not a keyword
Enter any word:True
Given word is keyword
Enter any word:return
Given word is keyword
Enter any word:string
Given word is not a keyword
'''
