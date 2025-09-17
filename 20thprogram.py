#  Total number of vowels
word = input("Enter a word: ").lower()# Take input and convert to lowercase
vowels = "aeiou" # List of vowels
count = 0 # Start counter at 0

for ch in word:# Go through each letter in the word
    if ch in vowels:# If the letter is a vowel
        count += 1# Increase the counter

print("Total vowels:", count)# Print total number of vowels