# Input matrix from user
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

print("Enter the matrix row by row:")
matrix = []
for i in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)

# Compute transpose
transpose = []
for j in range(cols):
    new_row = []
    for i in range(rows):
        new_row.append(matrix[i][j])
    transpose.append(new_row)

# Print result
print("\nOriginal Matrix:")
for row in matrix:
    print(row)

print("\nTranspose Matrix:")
for row in transpose:
    print(row)
