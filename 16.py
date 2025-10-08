# Input ages from user
ages = list(map(int, input("Enter ages separated by spaces: ").split()))

# Count persons in the range (60, 90)
count = 0
for age in ages:
    if age > 60 and age < 90:
        count += 1

print("Number of persons aged above 60 and below 90:", count)
