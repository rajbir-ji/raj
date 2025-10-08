# Function to multiply all numbers in a list
def multiply_list(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

# Take input from user
nums = list(map(int, input("Enter numbers separated by space: ").split()))

# Function call
product = multiply_list(nums)

# Display result
print(f"The product of all numbers in the list is: {product}")
