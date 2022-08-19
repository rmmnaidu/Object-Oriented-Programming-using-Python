#Pgm 4.6 Write a program to enter any character. If the entered character is in lowercase then convert it into uppercase character, then convert  it into lowercase.
ch = input("Enter any character:")
if(ch>='A' and ch<='Z'):
    ch = ch.lower()
    print("The entered character was in UPPERCASE. In LOWERCASE it is:"+ch)
else:
    ch = ch.upper()
    print("The entered character was in LOWERCASE. In UPPERCASE it is:"+ch)

'''
Output:
Enter any character:R
The entered character was in UPPERCASE. In LOWERCASE it is:r
Enter any character:r
The entered character was in LOWERCASE. In UPPERCASE it is:R
Enter any character:python
The entered character was in LOWERCASE. In UPPERCASE it is:PYTHON
Enter any character:PYTHON
The entered character was in UPPERCASE. In LOWERCASE it is:python
'''
