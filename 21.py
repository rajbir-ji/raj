# Input string
text = input("Enter a string: ")

# Check palindrome
if text == text[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is NOT a palindrome.")
