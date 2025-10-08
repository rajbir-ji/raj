import math

# Take inputs
x = float(input("Enter the value of x: "))
n = int(input("Enter the number of terms (n): "))

# (a) Series: x - x^2/2! + x^3/3! - x^4/4! + ... ± x^n/n!
sum_a = 0
for i in range(1, n+1):
    term = (x**i) / math.factorial(i)
    if i % 2 == 0:
        sum_a -= term
    else:
        sum_a += term

# (b) Series: x - x^3/3! + x^5/5! - x^7/7! + ... ± x^n/n!
sum_b = 0
for i in range(1, n+1, 2):  # only odd terms
    term = (x**i) / math.factorial(i)
    if (i // 2) % 2 == 0:   # alternate signs
        sum_b += term
    else:
        sum_b -= term

# Print results
print("Value of series (a):", sum_a)
print("Value of series (b):", sum_b)
