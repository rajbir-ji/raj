import math
numbers = list(map(float, input("Enter numbers separated by spaces: ").split()))
n = len(numbers)
product = 1
for num in numbers:
    product *= num
geometric_mean = product ** (1/n)
harmonic_mean = n / sum(1/num for num in numbers)
print("Geometric Mean:", geometric_mean)
print("Harmonic Mean:", harmonic_mean)
