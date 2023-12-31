import sys

input = sys.stdin.readline

shapes = [[(0,0),(0,1),(0,2),(0,3)],
        [(0,0),(1,0),(2,0),(3,0)],
        [(0,0),(1,0),(0,1),(1,1)],
        [(0,0),(1,0),(2,0),(2,1)],
        [(0,1),(1,1),(2,1),(2,0)],
        [(0,0),(0,1),(1,1),(2,1)],
        [(0,0),(0,1),(1,0),(2,0)],
        [(0,0),(1,0),(1,1),(1,2)],
        [(0,2),(1,1),(1,2),(1,0)],
        [(0,0),(0,1),(0,2),(1,2)],
        [(0,0),(1,0),(0,1),(0,2)],
        [(0,0),(1,0),(1,1),(2,1)],
        [(0,1),(1,1),(1,0),(2,0)],
        [(1,0),(1,1),(0,1),(0,2)],
        [(0,0),(0,1),(1,1),(1,2)],
        [(0,1),(1,0),(1,1),(1,2)],
        [(0,0),(0,1),(0,2),(1,1)],
        [(0,0),(1,0),(1,1),(2,0)],
        [(0,1),(1,1),(1,0),(2,1)]]

n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

max_val = 0

for x in range(n):
    for y in range(m):
        for shape in shapes:
            sum_val = 0
            for dx, dy in shape:
                if 0 <= x + dx < n and 0 <= y + dy < m:
                    sum_val += graph[x + dx][y + dy]
                else:
                    break
            else:
                max_val = max(max_val, sum_val)

print(max_val)