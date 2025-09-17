student_name=input("Enter the name of student:")

marks=[]
for i in range (3):
    mark=float(input(f"Enter the marks subjects {i+1}:"))
    marks.append(mark)
    print("marks of three subjects :",marks) 
    my_list=tuple(marks)
    print(my_list)
total_marks=my_list[0]+my_list[1]+my_list[2]
average_marks=total_marks/3
print("Total marks:",total_marks)
print("Average marks:",average_marks)
if average_marks>=90:
    grade="A"
elif average_marks>=75:
    grade="B"
elif average_marks>=50:
    grade="C"
else:
    grade="FAIL"
print("Grade:",grade)
student_set=set()
student_set.add(student_name)
print("\nStudent set:",student_set)
print("\nMarks one by one :")
for mark in marks:
    print(mark)
