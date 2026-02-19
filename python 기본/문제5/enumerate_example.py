fruits = ['사과', '바나나', '오렌지', '포도', '딸기']

print("기존 방식:")
for i in range(len(fruits)):
    print(f"{i}: {fruits[i]}")

print("\n과일 목록:")
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")