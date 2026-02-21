import math

def calculate_statistics(numbers):
    avg = sum(numbers) / len(numbers)
    
    maximum = max(numbers)
    minimum = min(numbers)
    
    variance = sum((x - avg) ** 2 for x in numbers) / len(numbers)
    std_dev = math.sqrt(variance)
    
    return avg, maximum, minimum, std_dev

data = [10, 20, 30, 40, 50]

average, high, low, sd = calculate_statistics(data)

print(f"숫자들: {data}")
print(f"평균: {average:.1f}")
print(f"최댓값: {high}")
print(f"최솟값: {low}")
print(f"표준편차: {sd:.2f}")