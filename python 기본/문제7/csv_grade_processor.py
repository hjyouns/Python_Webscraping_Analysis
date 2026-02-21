import csv

grade_data = [
    ['김철수', 85],
    ['이영희', 92],
    ['박민수', 78],
    ['최수진', 95]
]

with open('grades.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(grade_data)

print("학생 성적이 grades.csv에 저장되었습니다.\n")

total_score = 0
student_count = 0

print("성적 분석 결과:")
with open('grades.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        name = row[0]
        score = int(row[1]) 
        
        print(f"{name}: {score}점")
        
        total_score += score
        student_count += 1

if student_count > 0:
    average = total_score / student_count
    print(f"전체 평균: {average:.1f}점")