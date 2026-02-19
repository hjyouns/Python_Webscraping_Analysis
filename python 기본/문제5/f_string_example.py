import datetime

name, age = "김철수", 25
pi, price = 3.14159, 1234
percentage, today = 0.855, datetime.date(2025, 7, 20)

print(f"이름: {name}, 나이: {age}")
print(f"원주율: {pi:.2f}")           
print(f"가격: {price:,}원")        
print(f"퍼센트: {percentage:.2%}")    
print(f"날짜: {today:%Y년 %m월 %d일}") 