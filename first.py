# Arithmetic Operations Program

# Take input from the user
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

# Perform operations
sum_result = a + b
sub_result = a - b
mul_result = a * b
div_result = a / b if b != 0 else "Undefined (division by zero)"
exp_result = a ** b

# Display results
print("\n--- Arithmetic Results ---")
print(f"Sum: {sum_result}")
print(f"Subtraction: {sub_result}")
print(f"Multiplication: {mul_result}")
print(f"Division: {div_result}")
print(f"Exponentiation (a^b): {exp_result}")