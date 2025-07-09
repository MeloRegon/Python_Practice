# Geometry calculator for circle, rectangle, and right triangle.
# Calculates area, perimeter, and circumference based on user input.

import math

def calculate_circle(radius: float) -> tuple:
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return area, circumference

def calculate_rectangle(a: float, b:float) -> tuple:
    area = a * b
    perimeter = 2 * (a + b)
    return area, perimeter

def calculate_triangle(a: float, b:float) -> tuple:
    hypotenuse = math.sqrt(a ** 2 + b ** 2)
    area = 0.5 * a * b
    perimeter = a + b + hypotenuse
    return  area, perimeter, hypotenuse

print('Choose a shape to calculate:')
print('1. Circle')
print('2. Rectangle')
print('3. Right Triangle')

choice = input('Enter the number of your choice (1/2/3): ')

if choice == '1':
    radius = float(input('Enter the radius of the circle: '))
    area, circumference = calculate_circle(radius)
    print(f'Area: {area:.2f}\n'
          f'Circumference: {circumference:.2f}')

elif choice == '2':
    a = float(input('Enter side A of the rectangle: '))
    b = float(input('Enter side B of the rectangle: '))
    area, perimeter = calculate_rectangle(a, b)
    print(f'Area: {area:.2f}\n'
          f'Perimeter: {perimeter:.2f}')

elif choice == '3':
    a = float(input('Enter side A (first leg) of the triangle: '))
    b = float(input('Enter side B (second leg) of the triangle: '))
    area, perimeter, hypotenuse = calculate_triangle(a, b)
    print(f'Area: {area:.2f}\n'
          f'Perimeter: {perimeter:.2f}\n'
          f'Hypotenuse: {hypotenuse:.2f}')
else:
    print('Invalid choice.')