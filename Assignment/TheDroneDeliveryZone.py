n = int(input())
total = n * n

pairs = total * (total - 1) // 2

possible_moves = [(1, 2), (2, 1), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]

count = 0
for i in range(n):
    for j in range(n):
        for a, b in possible_moves:
            if 0 <= i + a < n and 0 <= j + b < n:
                count += 1
                
req = pairs - (count // 2)
print(round(req / pairs, 6))