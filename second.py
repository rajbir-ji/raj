import math

# Area Calculator Program

print("=== Area Calculator ===")

# Circle
radius = float(input("\nEnter radius of the circle: "))
circle_area = math.pi * radius ** 2
print(f"Area of Circle: {circle_area:.2f}")

# Rectangle
length = float(input("\nEnter length of the rectangle: "))
width = float(input("Enter width of the rectangle: "))
rectangle_area = length * width
print(f"Area of Rectangle: {rectangle_area:.2f}")

# Triangle
base = float(input("\nEnter base of the triangle: "))
height = float(input("Enter height of the triangle: "))
triangle_area = 0.5 * base * height
print(f"Area of Triangle: {triangle_area:.2f}")

# Square
side = float(input("\nEnter side of the square: "))
square_area = side ** 2
print(f"Area of Square: {square_area:.2f}")

# Trapezoid
base1 = float(input("\nEnter base1 of the trapezoid: "))
base2 = float(input("Enter base2 of the trapezoid: "))
height_trap = float(input("Enter height of the trapezoid: "))
trapezoid_area = (base1 + base2) * height_trap / 2
print(f"Area of Trapezoid: {trapezoid_area:.2f}")

# Parallelogram
base_para = float(input("\nEnter base of the parallelogram: "))
height_para = float(input("Enter height of the parallelogram: "))
parallelogram_area = base_para * height_para
print(f"Area of Parallelogram: {parallelogram_area:.2f}")
