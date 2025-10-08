# Function to count uppercase and lowercase letters
def count_case(string):
    upper = 0
    lower = 0
    
    for char in string:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
    
    print(f"Number of uppercase letters: {upper}")
    print(f"Number of lowercase letters: {lower}")

# Take input from user
text = input("Enter a string: ")

# Function call
count_case(text)
