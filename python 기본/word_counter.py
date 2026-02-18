sentence = input("문장을 입력하세요 : ")
words = sentence.split()

cleaned_sentence = " ".join(words)

print(f"공백 제거: {cleaned_sentence}")
print(f"단어 개수: {len(words)}개")