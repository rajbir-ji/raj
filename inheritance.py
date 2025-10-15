<<<<<<< HEAD
# a parent class : person(name, age)
# a child class : student(rollno, marks)
=======
#  inheritance
# a parent class :person(name,age)
# a child class :student(rollno,marks)
>>>>>>> 9d27e64965f9df267775c3ab8eedb43175241e15
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
<<<<<<< HEAD
        print(f"Name: {self.name}, Age: {self.age}")
=======
        print("Name:", self.name)
        print("Age:", self.age)
>>>>>>> 9d27e64965f9df267775c3ab8eedb43175241e15
class Student(Person):
    def __init__(self, name, age, rollno, marks):
        super().__init__(name, age)
        self.rollno = rollno
        self.marks = marks

    def display(self):
        super().display()
<<<<<<< HEAD
        print(f"Roll No: {self.rollno}, Marks: {self.marks}")
s1 = Student("Rajbir", 20, 101, 95)
s1.display()

=======
        print("Roll No:", self.rollno)
        print("Marks:", self.marks)
s1 = Student("Rajbir", 18, 52, 95)
s1.display()
>>>>>>> 9d27e64965f9df267775c3ab8eedb43175241e15
