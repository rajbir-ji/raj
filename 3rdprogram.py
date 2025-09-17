import math 
# CUBE
a=float(input(print("enter any number : ")))
volume_cube=a**3 
print("volume of cube is :",volume_cube) 
# CONE
r=float(input(print("enter the radius of Cone :")))
h=float(input(print("enter the height of Cone :")))
volume_cone=0.33*math.pi*r**2*h
print("volume of cone is :",volume_cone) 
# Volume: (1/3)πr²h 

# Cylinder
r1=float(input(print("enter the radius of Cylinder :")))
h1=float(input(print("enter the height of Cylinder :")))
volume_cylinder= math.pi*r1**2*h1
print("volume of cylinder is :",volume_cylinder) 
# Volume: πr²h
# Sphere
r2=float(input(print("enter the radius of Sphere :")))  
volume_sphere=(4/3)*math.pi*r2**3
print("volume of sphere is :",volume_sphere)