def create_sample_log():
    logs = [
        "2025-07-20 09:15:00 - WARNING - 메모리 사용량이 높습니다",
        "2025-07-20 10:30:00 - ERROR - 데이터베이스 연결 실패",
        "2025-07-20 11:45:00 - ERROR - 파일을 찾을 수 없음",
        "2025-07-20 12:00:00 - WARNING - 디스크 공간 부족",
        "2025-07-20 13:00:00 - INFO - 시스템이 정상 작동 중입니다"
    ]
    with open("system.log", "w", encoding="utf-8") as f:
        f.write("\n".join(logs))
    print("로그 파일이 생성되었습니다.\n")

def filter_logs(level):
    filtered_list = []
    with open("system.log", "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if f"- {level} -" in line:
                filtered_list.append(line)
    return filtered_list

create_sample_log()

print("ERROR 레벨 로그들:")
errors = filter_logs("ERROR")
for log in errors:
    print(log)

print("\nWARNING 레벨 로그들:")
warnings = filter_logs("WARNING")
for log in warnings:
    print(log)