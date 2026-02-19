students = ['김철수', '이영희', '박민수', '최수진']
scores = [85, 92, 78, 95]


print("기존 방식:")
for i in range(len(students)):
    print(f"{students[i]}: {scores[i]}점")

print("\n학생과 점수 매칭:")
for name, score in zip(students, scores):
    print(f"{name}: {score}점")

student_dict = dict(zip(students, scores))

print(f"\n점수별 학생 딕셔너리: {student_dict}")