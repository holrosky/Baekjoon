from collections import deque
import sys

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

input = sys.stdin.readline
n, m, k = map(int, input().split())

graph = [input().strip() for _ in range(n)]
visit = [[[0 for _ in range(m)] for _ in range(n)] for _ in range(k+1)]
queue = deque()

queue.append((0, 0, 0, 1))

while queue:
    x, y, t, c = queue.popleft()

    if (x, y) == (n-1, m-1):
        print(c)
        break

    for i in range(4):
        new_x = x + dx[i]
        new_y = y + dy[i]

        if 0 <= new_x < n and 0 <= new_y < m:
            if graph[new_x][new_y] == '0' and not visit[t][new_x][new_y]:
                visit[t][new_x][new_y] = 1
                queue.append((new_x, new_y, t, c+1))
            elif t < k and not visit[t][new_x][new_y]:
                visit[t][new_x][new_y] = 1
                queue.append((new_x, new_y, t+1, c+1))
else:
    print(-1)