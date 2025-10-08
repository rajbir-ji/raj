# file_name = input("Enter the file name (with extension): ")

# try:
    
#     with open(file_name, 'r') as file:
#         content = file.read()  
    
#     print("\n--- File Content ---")
#     print(content)
    
# except FileNotFoundError:
#     print(f"Error: The file '{file_name}' does not exist.")
# except Exception as e:
#     print(f"An error occurred: {e}")

# Ask user for the file name
file_name = input("Enter the file name (with extension): ")

# Ask user whether to create or read the file
choice = input("Do you want to create a new file? (yes/no): ").strip().lower()

if choice == 'yes':
    try:
        with open(file_name, 'w') as file:
            print(f"File '{file_name}' created successfully.")
            # Optionally allow user to add content while creating
            add_content = input("Do you want to add content to the file now? (yes/no): ").strip().lower()
            if add_content == 'yes':
                content = input("Enter content to write into the file:\n")
                file.write(content)
                print("Content added successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
else:
    # Read the existing file
    try:
        with open(file_name, 'r') as file:
            content = file.read()  # Read the entire file
        print("\n--- File Content ---")
        print(content)
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")
