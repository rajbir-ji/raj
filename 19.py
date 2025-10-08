# Count occurrence of vowels in a string
text = input("Enter string: ").lower()
vowels = "aeiou"
count = {v: text.count(v) for v in vowels}
print("Vowel counts:", count)