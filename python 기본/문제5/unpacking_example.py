point = {'x': 10, 'y': 20}
print(f"좌표: x={point['x']}, y={point['y']}")

a, b, c = [1, 2, 3]
print(f"리스트 언패킹: a={a}, b={b}, c={c}")

def sum_all(*args):
    return sum(args)

print(f"가변 인수의 합: {sum_all(10, 20, 30)}")

def print_info(**kwargs):
    result = ", ".join([f"{k}={v}" for k, v in kwargs.items()])
    print(f"키워드 인수들: {result}")

print_info(name="김철수", age=25, city="서울")