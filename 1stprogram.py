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
print("Sum: ",sum_result)
print("Subtraction: ",sub_result)
print("Multiplication: ",mul_result)
print("Division: ",div_result)
print("Exponentiation (a^b):" ,exp_result)