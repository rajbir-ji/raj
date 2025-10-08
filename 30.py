# Function to find maximum of three numbers
def find_max(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

# Take input from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

# Function call and display result
maximum = find_max(num1, num2, num3)
print(f"The maximum of the three numbers is: {maximum}")
