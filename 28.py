# Function to check if a number is in a given range
def check_range(num, start, end):
    if num in range(start, end + 1):
        print(f"{num} is in the range {start} to {end}.")
    else:
        print(f"{num} is NOT in the range {start} to {end}.")

# Taking input from user
num = int(input("Enter a number: "))
start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))

# Function call
check_range(num, start, end)
    