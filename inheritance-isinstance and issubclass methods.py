# Program to demonstrate isinstance() and issubclass() methods
class Person: # Here, Person is Base or Master or Parent class
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
class Teacher(Person): # Here, Teacher is derived class-1 and Person is Base class
    def __init__(self, name, age, experience, research_area):
        Person.__init__(self, name, age)
        self.experience = experience
        self.research_area = research_area
    def displaydata(self):
        Person.display(self)
        print("Experience:", self.experience)
        print("Research Area:", self.research_area)
class Student(Person): # Here, Student is derived class-2 and Person is Base class
    def __init__(self, name, age, course, year_semester):
        Person.__init__(self, name, age)
        self.course = course
        self.year_semester = year_semester
    def displaydata(self):
        Person.display(self)
        print("Course:", self.course)
        print("Year & Semester:", self.year_semester)
print("------TEACHER DETAILS------:")
T = Teacher("Dr. R. Madana Mohana", 42, 17, "Artificial Intelligence & Machine Learning")
T.displaydata()
print("------STUDENT DETAILS----:")
S = Student("RAM", 20, "B.E AI&DS-2", "I Year, II Semester")
S.displaydata()
print("------DEMO ON isinatnce() and issubclass() methods------:")
print("T is a Teacher?", isinstance(T, Teacher))
print("T is a Person?", isinstance(T, Person))
print("T is an Integer?", isinstance(T, int))
print("T is an Object?", isinstance(T, object))
print("Person is a subclass of Teacher?", issubclass(Person, Teacher))
print("Boolean is a subclass of int?", issubclass(bool, int))
'''
OUTPUT:
------TEACHER DETAILS------:
Name: Dr. R. Madana Mohana
Age: 42
Experience: 17
Research Area: Artificial Intelligence & Machine Learning
------STUDENT DETAILS----:
Name: RAM
Age: 20
Course: B.E AI&DS-2
Year & Semester: I Year, II Semester
------DEMO ON isinatnce() and issubclass() methods------:
T is a Teacher? True
T is a Person? True
T is an Integer? False
T is an Object? True
Person is a subclass of Teacher? False
Boolean is a subclass of int? True
'''
