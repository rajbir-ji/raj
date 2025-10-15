#  inheritance
# a parent class :person(name,age)
# a child class :student(rollno,marks)
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
class Student(Person):
    def __init__(self, name, age, rollno, marks):
        super().__init__(name, age)
        self.rollno = rollno
        self.marks = marks

    def display(self):
        super().display()
        print("Roll No:", self.rollno)
        print("Marks:", self.marks)
s1 = Student("Rajbir", 18, 52, 95)
s1.display()
