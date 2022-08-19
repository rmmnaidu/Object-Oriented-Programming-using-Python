# Program to illustrate static method
class Choice:
    def __init__(self, subjects):
        self.subjects = subjects
    @staticmethod
    def validate_subject(subjects):
        if "CSA" in subjects:
            print("This option is no longer available..")
        else:
            return True
subjects = ["DS", "CSA", "FoC", "OS", "TOC"]
if all(Choice.validate_subject(i) for i in subjects):
    ch = Choice(subjects)
    print("You have been allotted the subjects: ",subjects)

'''
OUTPUT:
This option is no longer available..
'''

    
