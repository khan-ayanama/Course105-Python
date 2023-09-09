# Association and Aggregation: OOP also allows you to model relationships between objects. Association represents a relationship between objects, while aggregation represents a "whole-part" relationship, where one object is composed of other objects.

# Association represents a relationship between two or more objects where they are loosely connected and can exist independently. Here's an example of association:

class Teacher:
    def __init__(self, name):
        self.name = name

    def teach(self, subject):
        print(f"{self.name} teaches {subject}")

class Student:
    def __init__(self, name):
        self.name = name

    def learn(self, subject):
        print(f"{self.name} learns {subject}")

# Creating instances of Teacher and Student
teacher = Teacher("Mrs. Smith")
student = Student("Alice")

# Associating the teacher and student
teacher.teach("Math")
student.learn("Math")

# We have two classes, Teacher and Student, representing a teacher and a student.

# These classes are associated because a teacher can teach multiple students, and a student can have multiple teachers.

# The objects teacher and student are loosely connected but can exist independently.


# Aggregation represents a "whole-part" relationship between objects, where one object is composed of or contains other objects. Here's an example of aggregation:

class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

class Employee:
    def __init__(self, name):
        self.name = name

# Creating instances of Employee and Department
employee1 = Employee("Alice")
employee2 = Employee("Bob")
department = Department("HR")

# Aggregating employees into the department
department.add_employee(employee1)
department.add_employee(employee2)

# Accessing employees in the department
for employee in department.employees:
    print(f"{employee.name} works in the {department.name} department")



