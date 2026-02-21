# 1. 숫자 목록 리스트 생성
numbers = [15, 3, 27, 8, 19, 12, 31]

# 2. 최댓값과 최솟값 구하기 (내장 함수 사용)
max_val = max(numbers)
min_val = min(numbers)

# 3. 두 번째로 큰 값 구하기
# 리스트를 복사한 뒤 내림차순으로 정렬 (원본 유지를 위해 sorted 사용)
sorted_numbers = sorted(numbers, reverse=True)
second_max = sorted_numbers[1]

# 4. 결과 출력
print(f"숫자 목록: {numbers}")
print(f"최댓값: {max_val}")
print(f"최솟값: {min_val}")
print(f"두 번째로 큰 값: {second_max}")