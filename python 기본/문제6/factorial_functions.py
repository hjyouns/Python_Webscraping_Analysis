def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)

def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

test_cases = [5, 7]

for num in test_cases:
    res_rec = factorial_recursive(num)
    res_ite = factorial_iterative(num)
    print(f"{num}! (재귀) = {res_rec}")
    print(f"{num}! (반복) = {res_ite}")