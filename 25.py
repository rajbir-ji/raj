# Program to perform Sequential Search on an ordered list

# Take input from user
numbers = list(map(int, input("Enter numbers in ascending order: ").split()))

# Take the element to search
key = int(input("Enter the number to search: "))

# Sequential search logic (optimized for ordered list)
found = False
for i in range(len(numbers)):
    if numbers[i] == key:
        print(f"Element {key} found at position {i + 1}.")
        found = True
        break
    elif numbers[i] > key:
        # Since list is ordered, no need to check further
        break

if not found:   
    print(f"Element {key} not found in the list.")
