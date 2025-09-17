word = input("Enter a word: ").lower() # Take input and convert to lowercase
vowels = "aeiou"# List of vowels

for v in vowels: # Loop through each vowel
    count = word.count(v)# Count how many times the vowel appears
    if count > 0:# If the vowel is present
        print(v, ":", count)