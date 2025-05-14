## INFINITY STONES


from collections import deque 
n = int(input())
grid = [list(input()) for _ in range(n)]
visited = set()
gems = set([(i, j) for i in range(n) for j in range(n) if grid[i][j] == "*"])
dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

visited.add((0, 0, tuple()))
q = deque([(0, 0, 0, set())])
while q:
    x, y, dist, collected = q.popleft()
    
    if (x, y) == (n - 1, n - 1) and collected == gems:
        print(dist)
        exit()
    
    for dx, dy in dirs:
        nx = x + dx 
        ny = y + dy 
        if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] != "#":
            new_collected = collected.copy()
            if grid[nx][ny] == "*":
                new_collected.add((nx, ny))
            
            curr = (nx, ny, tuple(new_collected))
            if curr not in visited:
                visited.add(curr)
                q.append((nx, ny, dist + 1, new_collected))
print(-1)


#Divide Two Integers
a, b = map(int, input().split())
neg = (a < 0) ^ (b < 0)

a = abs(a)
b = abs(b)

print((a // b) * (-1 if neg else 1))