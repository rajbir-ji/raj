class StringReverser:
    def __init__(self, text):
        self.text = text

  
    def reverse_words(self):
        words = self.text.split()       
        reversed_words = words[::-1]    
        return ' '.join(reversed_words) 


sentence = input("Enter a string: ")


reverser = StringReverser(sentence)

print("Reversed string (word by word):")
print(reverser.reverse_words())
