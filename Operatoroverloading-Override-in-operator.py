# Program to override the in operator
class marks:
    def __init__(self):
        self.max_marks = {"OOPP":100, "DSA":90, "DEE":85, "CHEMISTRY":80}
    def __contains__(self, sub):
        if sub in self.max_marks:
            return True
        else:
            return False
    def __getitem__(self, sub):
        return self.max_marks[sub]
    def __str__(self):
        return "The dictionary contains the names of subjects and maximum marks allotted to them"
M = marks()
print(str(M))
sub = input("Enter the subject for which you want to know extra marks..")
if sub in M:
    print("OOPP paper has maximum marks allotted = ", M[sub])

'''
OUTPUT:
The dictionary contains the names of subjects and maximum marks allotted to them
Enter the subject for which you want to know extra marks..DSA
OOPP paper has maximum marks allotted =  90
'''

        
       
