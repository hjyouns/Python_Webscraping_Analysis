PI = 3.14159
Radius = float(input("원의 반지름을 입력하세요:"))

area = PI * (Radius ** 2)
circumference = 2 * PI * Radius


print(f"반지름이 {Radius}인 원의 넓이 :{area} ")
print(f"반지름이 {Radius}인 원의 둘레 :{circumference}")
