content = "안녕하세요\n파이썬 파일 처리를 연습하고 있습니다\n오늘은 좋은 날씨입니다"

print("파일에 저장할 내용:")
print(content)

with open("test.txt", "w", encoding="utf-8") as f:
    f.write(content)

print("\n" + "-"*20 + "\n")

print("파일에서 읽어온 내용:")
with open("test.txt", "r", encoding="utf-8") as f:
    data = f.read()
    print(data)