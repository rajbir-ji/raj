# traversal is the process of acessing each 
# elements of a data structure exactly once
#  so that we can perform some operation on it.
# traversal insertion,deletion,searching,updating
arr=[10,20,30,40,50]
print(" Linear Traversal:")
for i in arr:
    print(i,end="")
print()
# deletion
arr.remove(30)
print("After deletion:")
for i in arr:
    print(i,end="")
print()
# clearing
arr.clear()
print("After clearing:")
for i in arr:
    print(i,end="")
print()
# appending
arr.append(60)
print("After insertion:")
for i in arr:
    print(i,end="")
print()
# insertion
arr.insert(2,25)
print("After insertion at index 2:")
for i in arr:
    print(i,end="")
# extending 
arr.extend([70,80])
print("After extending:")
for i in arr:
    print(i,end="")
    # taversal reverse
arr.reverse()
print("After reversing:")
for i in arr:
    print(i,end="")
