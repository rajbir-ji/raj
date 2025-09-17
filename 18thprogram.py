# Program to perform addition, subtraction and multiplication on two matrices
# Define two matrices
A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
B = [[9, 8, 7],
     [6, 5, 4],
     [3, 2, 1]]
# Addition
add = [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
# Subtraction
sub = [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
# Multiplication
mul = [[sum(A[i][k] * B[k][j] for k in range(len(A))) for j in range(len(B[0]))] for i in range(len(A))]
# Display results
print("Matrix A:")
for row in A:
    print(row)
print("\nMatrix B:")
for row in B:
    print(row)
print("\nAddition of A and B:")
for row in add:
    print(row)
print("\nSubtraction of A and B:")
for row in sub:
    print(row)
print("\nMultiplication of A and B:")
for row in mul:
    print(row)