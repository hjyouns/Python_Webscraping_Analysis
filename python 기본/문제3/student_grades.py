grades = {
    "김철수": 85,
    "이영희": 92,
    "박민수": 78,
    "최수진": 95
}

print("학생 성적:")
for name, score in grades.items():
    print(f"{name}: {score}점")


total_score = sum(grades.values())
average_score = total_score / len(grades)

# 4. 결과 출력
print(f"평균 점수: {average_score}점")