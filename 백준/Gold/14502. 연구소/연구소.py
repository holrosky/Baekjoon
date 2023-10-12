import sys
from collections import deque
from copy import deepcopy

input = sys.stdin.readline

answer = 0

n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for i in range(n*m):
    if graph[(i-1)//m][(i-1)%m]:
        continue
    for j in range(i+1, n*m):
        if graph[(j - 1) // m][(j - 1) % m]:
            continue
        for k in range(j+1, n*m):
            if graph[(k - 1) // m][(k - 1) % m]:
                continue

            temp = deepcopy(graph)
            temp[(i - 1) // m][(i - 1) % m] = 1
            temp[(j - 1) // m][(j - 1) % m] = 1
            temp[(k - 1) // m][(k - 1) % m] = 1

            queue = deque()
            temp_sum = 0
            for x in range(n):
                for y in range(m):
                    if temp[x][y] == 2:
                        queue.append((x, y))

            while queue:
                cx, cy = queue.popleft()

                for z in range(4):
                    nx = cx + dx[z]
                    ny = cy + dy[z]

                    if 0 <= nx < n and 0 <= ny < m and not temp[nx][ny]:
                        queue.append((nx, ny))
                        temp[nx][ny] = 2


            for x in range(n):
                for y in range(m):
                    if not temp[x][y]:
                        temp_sum += 1

            answer = max(answer, temp_sum)

print(answer)