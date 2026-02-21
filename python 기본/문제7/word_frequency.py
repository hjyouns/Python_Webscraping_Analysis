sample_text = "파이썬 프로그래밍 언어 파이썬 배우기 쉬운 언어 파이썬 강력한 프로그래밍"
with open("data.txt", "w", encoding="utf-8") as f:
    f.write(sample_text)

word_counts = {}

with open("data.txt", "r", encoding="utf-8") as f:
    content = f.read()
    words = content.split()

for word in words:
    word_counts[word] = word_counts.get(word, 0) + 1

print("단어 빈도 분석 결과:")
sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

for word, count in sorted_words:
    print(f"{word}: {count}번")