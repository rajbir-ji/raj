# Function to check prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):  # check up to sqrt(num)
        if num % i == 0:
            return False
    return True

# Input range from user
start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))

print(f"Prime numbers between {start} and {end}:")
for num in range(start, end + 1):
    if is_prime(num):
        print(num, end=" ")
