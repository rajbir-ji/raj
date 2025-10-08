import math

side=float(input("Enter the side of the cube: "))
volume_cube=side**3
print(f"Volume of cube is {volume_cube}")

radius=float(input("Enter the radius for cylinder: "))
height=float(input("Enter the height of the cylinder: "))
volume_cylinder=math.pi*radius**2*height
print(f"Volume of the cylinder is {volume_cylinder}")

radius1=float(input("Enter the radius of the cone: "))
height1=float(input("Enter the height of the cone: "))
volume_cone=0.33*math.pi*radius1**2*height1
print(f"Volume of the cone is {volume_cone}")

radius2=float(input("Enter the radius of the sphere: "))
volume_sphere=1.33*math.pi*radius2**3
print(f"Volume of the sphere is {volume_sphere}")
