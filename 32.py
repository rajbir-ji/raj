# Recursive function to print Fibonacci sequence
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Take input from user
terms = int(input("Enter the number of terms: "))

# Check for valid input
if terms <= 0:
    print("Please enter a positive integer.")
else:
    print("Fibonacci sequence:")
    for i in range(terms):
        print(fibonacci(i), end=" ")
