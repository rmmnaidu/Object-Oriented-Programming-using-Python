# Program to demonstrate the use of inheritance
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
print(Student.__base__) # To display base class of Studnet class
print(Teacher.__base__) # To display base class of Studnet class
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
<class '__main__.Person'>
'''
