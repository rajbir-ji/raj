# Ask user for the file name
file_name = input("Enter the file name (with extension): ")

# Ask user how many lines to read
n = int(input("Enter the number of lines to read: "))

try:
    # Open the file in read mode
    with open(file_name, 'r') as file:
        print(f"\n--- First {n} lines of the file ---")
        for i in range(n):
            line = file.readline()
            if not line:  # If end of file is reached
                break
            print(line, end='')  # end='' to avoid double newlines

except FileNotFoundError:
    print(f"Error: The file '{file_name}' does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")
