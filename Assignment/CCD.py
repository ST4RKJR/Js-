import math

n = int(input())
scores = list(map(int, input().split()))

mean = sum(scores) / n

variance = sum((x - mean) ** 2 for x in scores) / n

std_dev = math.sqrt(variance)

print(f"{std_dev:.2f}")