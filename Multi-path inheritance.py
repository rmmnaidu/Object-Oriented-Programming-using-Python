# Program to demonstrate multi-path inheritance
class Student: # Base class
    def name(self):
        print("Name:")
class Academic_Performance(Student): # Derived Class1 from Base Class Student
    def Academic_Score(self):
        print("Overall CGPA is 9.7 and above out of 10")
class Written_Test(Student): # Derived Class2 from Base Class Student
    def Written_test_Score(self):
        print("Written Test Score is 65% and above")
class Result(Academic_Performance, Written_Test ): # Derived Class3 from Derived Classes Academic_Performance & Written_Test
    def Eligibility(self):
        print("---Minimum Eligibility to Apply for Placements in Core Tier-1 Companies----")
        self.Academic_Score()
        self.Written_test_Score()
r1 = Result()
r1.Eligibility()

'''
OUTPUT:
---Minimum Eligibility to Apply for Placements in Core Tier-1 Companies----
Overal CGPA is 9.7 and above out of 10
Written Test Score is 65% and above
'''

