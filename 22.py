# Initial list
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
print("Original List:", numbers)

# 1) Insert an element
element = int(input("\nEnter element to insert: "))
pos = int(input("Enter position (0-based index): "))
numbers.insert(pos, element)
print("List after insertion:", numbers)

# 2) Delete an element
del_element = int(input("\nEnter element to delete: "))
if del_element in numbers:
    numbers.remove(del_element)
    print("List after deletion:", numbers)
else:
    print("Element not found in list!")

# 3) Sort the list
numbers.sort()
print("\nSorted List:", numbers)

# 4) Delete entire list
numbers.clear()
print("List after deleting all elements:", numbers)
