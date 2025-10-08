# Print numbers up to N which are not divisible by 3, 6, 9,, e.g., 1, 2, 4, 5, 7,….
n=int(input("Enter n numbers: "))
for i in range(1,n+1):
    if i%3!=0 and i%6!=0 and i% 9!=0:
        print(i, end=" ")