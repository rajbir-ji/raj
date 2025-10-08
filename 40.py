# Ask user for the file name
file_name = input("Enter the file name (with extension): ")

# Option to write new content
write_choice = input("Do you want to write new content? (yes/no): ").strip().lower()
if write_choice == 'yes':
    with open(file_name, 'w') as file:
        content = input("Enter content to write into the file:\n")
        file.write(content + "\n")
        print(f"Content written to '{file_name}' successfully.")

# Option to append content
append_choice = input("Do you want to append content? (yes/no): ").strip().lower()
if append_choice == 'yes':
    with open(file_name, 'a') as file:
        content = input("Enter content to append to the file:\n")
        file.write(content + "\n")
        print(f"Content appended to '{file_name}' successfully.")

# Display the content of the file
print(f"\n--- Displaying content of '{file_name}' ---")
try:
    with open(file_name, 'r') as file:
        print(file.read())
except FileNotFoundError:
    print(f"Error: The file '{file_name}' does not exist.")
