import math
x, n = int(input("x: ")), int(input("n: "))
s1 = sum([((-1)**(i+1)) * (x**i)/math.factorial(i) for i in range(1, n+1)])
s2 = sum([((-1)*((i-1)//2)) * (x**i)/math.factorial(i) for i in range(1, n+1, 2)])
print("Series a =", s1)
print("Series b =", s2)
