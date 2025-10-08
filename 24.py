numbers = list(map(int, input("Enter numbers separated by space: ").split()))

# Take the element to search
key = int(input("Enter the number to search: "))
found = False
for i in range(len(numbers)):
    if numbers[i] == key:
        print(f"Element {key} found at position {i + 1}.")
        found = True
        break

if not found:
    print(f"Element {key} not found in the list.")
