a, b = map(float, input().split())
r = (1 - a) * (1 - b)
print(round(a / (1 - r),6))