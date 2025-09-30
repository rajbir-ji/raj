nums=list(map(float,input("Enter a number: ").split()))
n=len(nums)
g_mean=1
for x in nums:g_mean*=x
g_mean=g_mean**(1/n)
h_means=n/sum(1/x for x in nums)
print("Geometric Mean:",g_mean)
print("Harmonic Mean:",h_means)
