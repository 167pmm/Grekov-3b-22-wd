class Student:

    def __init__(self, name, lastname, group, grades):
        self.name = name
        self.lastname = lastname
        self.group = group
        self.grades = grades

    def gpa(self):
        return sum(self.grades) / len(self.grades)


student = Student("Герман", "Греков", "OD-22-WD", [5, 4, 5, 5])
print(student.gpa())