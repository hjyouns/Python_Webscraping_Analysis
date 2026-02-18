original_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

unique_elements = set(original_list)

result_list = sorted(list(unique_elements))

print(f"원본 리스트: {original_list}")
print(f"중복 제거 후: {result_list}")