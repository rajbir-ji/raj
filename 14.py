import itertools

numbers = [4, 5, 6]

print("All permutations (arrangements):")
for p in itertools.permutations(numbers, 3):
    print(p)

print("\nAll combinations (unordered groups):")
for c in itertools.combinations(numbers, 2):  # choose 2 at a time
    print(c)
for c in itertools.combinations(numbers, 3):  # choose all 3
    print(c)
