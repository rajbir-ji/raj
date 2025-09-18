# 14.Program to print all permutations of 4, 5, 6 without using library
def permute(s):
    if len(s) == 0:
        return ['']
    result = []
    for i, char in enumerate(s):
        for p in permute(s[:i] + s[i+1:]):
            result.append(char + p)
    return result
print(permute("456"))