import math 
a=int(input("Enter the value (a):"))
b=int(input("Enter the value (b):"))
c=int(input("Enter the value (c):")) 
d=(b**2) - (4*a*c)  
if d >=0:
    root1=(-b+math.sqrt(d))/(2*a)
    root2=(-b-math.sqrt(d))/(2*a)
    print("Roots are real and different.")
    print(f"Root 1: {root1}")
    print(f"Root 2: {root2}")
else:
    real_part = -b / (2 * a)
    imaginary_part = math.sqrt(-d) / (2 * a)
    print("Roots are complex and different.")
    print(f"Root 1: {real_part} + {imaginary_part}i")
    print(f"Root 2: {real_part} - {imaginary_part}i")
    
     

