# a parent class : person(name, age)
# a child class : student(rollno, marks)
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")
class Student(Person):
    def __init__(self, name, age, rollno, marks):
        super().__init__(name, age)
        self.rollno = rollno
        self.marks = marks

    def display(self):
        super().display()
        print(f"Roll No: {self.rollno}, Marks: {self.marks}")
s1 = Student("Rajbir", 20, 101, 95)
s1.display()

