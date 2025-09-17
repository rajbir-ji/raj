n=int(input("Enter number :"))
a=0
b=1 
print("Fibonacci series:")
for i in range(n):  
    print(a,end='\n')
    c=a+b
    a=b
    b=c
    # print(f"{a}+{i}={c}")  
