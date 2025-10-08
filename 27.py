student = {}

# 1️⃣ Insert Operation
n = int(input("Enter number of records to insert: "))
for i in range(n):
    roll_no = input(f"\nEnter roll number for student {i+1}: ")
    name = input("Enter student name: ")
    student[roll_no] = name

print("\nDictionary after insertion:")
print(student)

# 2️⃣ Delete Operation
del_key = input("\nEnter roll number to delete: ")
if del_key in student:
    del student[del_key]
    print(f"Record with roll number {del_key} deleted successfully.")
else:
    print("Roll number not found!")

print("\nDictionary after deletion:")
print(student)

# 3️⃣ Change (Update) Operation
update_key = input("\nEnter roll number to update: ")
if update_key in student:
    new_name = input("Enter new name: ")
    student[update_key] = new_name
    print(f"Record with roll number {update_key} updated successfully.")
else:
    print("Roll number not found!")

print("\nFinal Dictionary after update:")
print(student)
