class stdudent:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name: ",self.name)
        print("Age: ",self.age)
s1 = stdudent("Rajbir", 19)
s2 = stdudent("Kartikay", 20)
s1.display()
s2.display()