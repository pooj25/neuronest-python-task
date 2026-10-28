
class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def display_details(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)

    def is_adult(self):
        return self.age >= 18


student1 = Student("Pooja", 21, "CSBS")
student2 = Student("Priya", 20, "CSE")

print("Student 1 Details")
student1.display_details()
print("Adult:", student1.is_adult())

print("\nStudent 2 Details")
student2.display_details()
print("Adult:", student2.is_adult())
