# Dictionary in Python
# A dictionary is a collection of key-value pairs.
student_dictionary = {
    "name": "Rajbir Singh",
    "Class": "BCA-3rd",
    "Roll no": "2439052",
    "Phone no": "7740012175",
    "Age": 19,
    "Height": 5.7,
    "Address": "jalandhar",
    "Email": "sandhurajbir8085@gmail.com"
}
print(student_dictionary["name"])
# Accessing value using get() method
print(student_dictionary.get("Class"))
# keys() method to get all keys in the dictionary 
print(student_dictionary.keys())
# values() method to get all values in the dictionary
print(student_dictionary.values())
# items() method to get all key-value pairs in the dictionary
print(student_dictionary.items())
student_dictionary["Age"] = 20  # Updating value for key 'Age'
print(student_dictionary)
student_dictionary.setdefault("Phone no", "7740012175")  # Will not change as key exists
print(student_dictionary) 
student_dictionary.update({"Phone no": "7740049847"}) 
print(student_dictionary)
student_dictionary.pop("Height")  # Removes the key 'Height'
print(student_dictionary)
student_dictionary.popitem()  # Removes the last inserted key-value pair
print(student_dictionary)
del student_dictionary["Roll no"]  # Deletes the key 'Roll no'
print(student_dictionary)
student_dictionary.clear()  # Clears the dictionary
print(student_dictionary)  # Output will be {}
student_dictionary.copy()  # Returns a shallow copy of the dictionary
print(student_dictionary)  # Output will be {}
student_dictionary.fromkeys(["name", "Class"])  # Creates a new dictionary with specified keys and None values
print(student_dictionary)  # Output will be {}


