# Get user input for integer and floating-point numbers
a = float(input("Enter a number (a): "))
b = float(input("Enter another number (b): "))
c = int(input("Enter an integer (c): "))

# Perform arithmetic operations
sum_ab = a + b
difference_ac = a - c
product_bc = b * c
quotient_ab = a / b
modulus_ab = a % b
exponentiation_ab = a ** b

# Print the results
print("a + b =", sum_ab)
print("a - c =", difference_ac)
print("b * c =", product_bc)
print("a / b =", quotient_ab)
print("a % b =", modulus_ab)
print("a ** b =", exponentiation_ab)

# Use built-in functions for numerical operations
absolute_c = abs(c)
rounded_b = round(b)
max_value = max(a, b, c)
min_value = min(a, b, c)

print("Absolute value of c:", absolute_c)
print("Rounded value of b:", rounded_b)
print("Max value:", max_value)
print("Min value:", min_value)

# Import the math module for more advanced math operations
import math

square_root_a = math.sqrt(a)
logarithm_base_10_a = math.log10(a)
factorial_c = math.factorial(abs(c))

print("Square root of a:", square_root_a)
print("Logarithm base 10 of a:", logarithm_base_10_a)
print(f"Factorial of |c| ({abs(c)}):", factorial_c)

# Additional feature: Check if a number is even or odd
def check_even_odd(num):
    if num % 2 == 0:
        return "even"
    else:
        return "odd"

print(f"a is {check_even_odd(a)}")
print(f"b is {check_even_odd(b)}")
print(f"c is {check_even_odd(c)}")

# Additional feature: Calculate the area of a rectangle using user input
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
area_rectangle = length * width
print("Area of the rectangle:", area_rectangle)

# Additional feature: Convert temperature from Celsius to Fahrenheit
celsius_temp = float(input("Enter temperature in Celsius: "))
fahrenheit_temp = (celsius_temp * 9/5) + 32
print("Temperature in Fahrenheit:", fahrenheit_temp)


