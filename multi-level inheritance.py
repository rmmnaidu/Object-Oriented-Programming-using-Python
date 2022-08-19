# Program to implement mult-level inheritance
class Person: # Base class
    def name(self):
        faculty_name = input("Enter Eligible Faculty Name for HOD position..\n")
        print("Name:", faculty_name)
class Teacher(Person):# Class Teacher derived from the Base class Person
    def Qualification(self):
        print("Qualification of HOD is Ph.D mandatory:")
class HOD(Teacher): # Class HOD is derived from the Derived class Teacher
    def Experience(self):
        print("Experience of HOD is at least 15 years:")
        print(HOD.__mro__)
h = HOD()
h.name()
h.Qualification()
h.Experience()
'''
OUTPUT:
Enter Eligible Faculty Name for HOD position..
Dr R MADANA MOHANA
Name: Dr R MADANA MOHANA
Qualification of HOD is Ph.D mandatory:
Experience of HOD is at least 15 years:
(<class '__main__.HOD'>, <class '__main__.Teacher'>, <class '__main__.Person'>, <class 'object'>)<class 'object'>)
'''
