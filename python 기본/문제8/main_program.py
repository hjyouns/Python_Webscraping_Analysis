import math_operations

circle = math_operations.get_circle_area(5)
rect = math_operations.get_rectangle_area(10, 5)
fact = math_operations.get_factorial(5)
gcd_val = math_operations.get_gcd(48, 18)

print(f"원의 넓이: {circle:.2f}")
print(f"직사각형 넓이: {rect}")
print(f"팩토리얼 5! = {fact}")
print(f"최대공약수(48, 18) = {gcd_val}")