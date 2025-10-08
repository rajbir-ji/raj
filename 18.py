# Input dimensions
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

print("Enter elements of first matrix:")
A = []
for i in range(rows):
    A.append(list(map(int, input().split())))

print("Enter elements of second matrix:")
B = []
for i in range(rows):
    B.append(list(map(int, input().split())))

# 1) Addition
add = [[A[i][j] + B[i][j] for j in range(cols)] for i in range(rows)]

# 2) Subtraction
sub = [[A[i][j] - B[i][j] for j in range(cols)] for i in range(rows)]

# 3) Multiplication (Matrix product)
mul = [[0 for _ in range(cols)] for _ in range(rows)]
for i in range(rows):
    for j in range(cols):
        for k in range(cols):
            mul[i][j] += A[i][k] * B[k][j]

# Output results
print("\nMatrix A:")
for row in A:
    print(row)

print("\nMatrix B:")
for row in B:
    print(row)

print("\nAddition of matrices:")
for row in add:
    print(row)

print("\nSubtraction of matrices:")
for row in sub:
    print(row)

print("\nMultiplication of matrices:")
for row in mul:
    print(row)
