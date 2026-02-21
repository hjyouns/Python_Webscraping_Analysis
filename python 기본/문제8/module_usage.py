import datetime
import random

now = datetime.datetime.now()
print(f"현재 날짜와 시간: {now.strftime('%Y-%m-%d %H:%M:%S')}")

weekdays = ['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일']
weekday_name = weekdays[now.weekday()]

formatted_date = now.strftime(f"%Y년 %m월 %d일 {weekday_name}")
print(f"포맷된 날짜: {formatted_date}")

fruits = ['사과', '바나나', '오렌지', '포도', '딸기']

print(f"임의의 숫자: {random.randint(1, 10)}")      
print(f"임의의 실수: {random.uniform(1, 10):.2f}")   
print(f"임의의 리스트 요소: {random.choice(fruits)}") 

random.shuffle(fruits)
print(f"섞인 리스트: {fruits}")