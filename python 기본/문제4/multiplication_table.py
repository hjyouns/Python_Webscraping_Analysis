number = int(input("몇단을 출력할까요?"))

print(f"{number}단 구구단")

for i in range(1,10):
    result = number * i
    print(f"{number} X {i} = {result}")

