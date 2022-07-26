# note: working directory will have to be class_object for this to work
from class_object import Student, Teacher

# name, major, GPA, probation
student1 = Student("Kylie", "Business", 3.4, False)
student2 = Student("Drew", "Business", 1.8, True)

print(student1.name)
print(student2.name)

# name, coursenum
teacher1 = Teacher("Ms. Pam", "CS348")

print(teacher1.name + " " + teacher1.coursenum)