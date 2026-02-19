# 1. 3의 배수를 담을 빈 리스트 생성
multiples = []

# 2. 1부터 100까지 반복 (range의 끝 값은 포함되지 않으므로 101까지 설정)
for i in range(1, 101):
    # 3. 3으로 나눈 나머지가 0이면 3의 배수
    if i % 3 == 0:
        multiples.append(i)

# 4. 합계와 개수 계산
total_sum = sum(multiples)
total_count = len(multiples)

# 5. 결과 출력
print(f"1부터 100까지 3의 배수: {multiples}")
print(f"3의 배수의 합: {total_sum}")
print(f"3의 배수의 개수: {total_count}개")