def greet(name, greeting="안녕하세요", suffix=""):
    if suffix:
        return f"{greeting}, {name}님! {suffix}"
    
    if greeting == "Hello":
        return f"{greeting}, {name}!"
    
    return f"{greeting}, {name}님!"

print(greet("김철수"))

print(greet("John", greeting="Hello"))

print(greet("이영희", suffix="좋은 하루 되세요!"))