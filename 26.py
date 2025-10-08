library = {}

# Take number of notebooks
n = int(input("Enter number of notebooks to add: "))

# Add notebook records
for i in range(n):
    serial_no = input(f"\nEnter serial number for notebook {i+1}: ")
    name = input("Enter student's name: ")
    subject = input("Enter subject name: ")
    
    # Store details in dictionary
    library[serial_no] = {'Name': name, 'Subject': subject}

# Display all records
print("\n--- Library Practical Notebook Records ---")
for serial, details in library.items():
    print(f"Serial No: {serial}")
    print(f"  Name: {details['Name']}")
    print(f"  Subject: {details['Subject']}")
    print("--------------------------------------")

# Search for a notebook by serial number
search_serial = input("\nEnter serial number to search: ")
if search_serial in library:
    print(f"\nNotebook found for Serial No {search_serial}:")
    print(f"Name: {library[search_serial]['Name']}")
    print(f"Subject: {library[search_serial]['Subject']}")
else:
    print("\nNotebook not found in the library records.")
