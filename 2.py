import math
def area_circle(radius):
    return math.pi*radius**2
def area_rectangle(length,breadth):
    return length*breadth
def area_triangle(base,height):
    return 0.5*base*height
def area_square(side):
    return side**2
def area_trapezoid(base1,base2,height):
    return 0.5*(base1+base2)*height
def area_parallelogram(base,height):
    return base*height


radius=float(input("Enter the radius of the circle: "))
print(f"Area of circle: {area_circle(radius)}")
length=float(input("Enter the length of the rectangle: "))
breadth=float(input("Enter the breadth of the rectangle: "))
print(f"Area of rectangle: {area_rectangle(length,breadth)}")
base=float(input("Enter the base of the triangle: "))
height1=float(input("Enter the height of the triangle"))
print(f"Area of triangle: {area_triangle(base,height1)}")
side=float(input("Enter the side of the square: "))
print(f"Area of square: {area_square(side)}")
base1=float(input("Enter the base1 of the trapezoid: "))
base2=float(input("Enter the base2 of the trapezoid: "))
height2=float(input("Enter the height of the trapezoid: "))
print(f"Area of the trapezoid: {area_trapezoid(base1,base2,height2)}")
base3=float(input("Enter the base of the parallelogram: "))
height3=float(input("Enter the height of the parallelogram: "))
print(f"Area of the parallelogram: {area_parallelogram(base3,height3)}")



