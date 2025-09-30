rows,cols=2,3
matrix=[[int(input(f"Enter element {i+1},{j+1}: ")) 
         for j in range(cols)] for i in range(rows)]
print("Matrix:")