# Input word
word = input("Enter a word: ")

# Define vowels
vowels = "aeiouAEIOU"

# Count vowels
count = 0
for ch in word:
    if ch in vowels:
        count += 1

print("Total number of vowels:", count)
