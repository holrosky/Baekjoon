import sys
from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

w, h = map(int, sys.stdin.readline().split())

graph = [list(sys.stdin.readline().rstrip()) for _ in range(h)]

laser_loc = []

for x in range(h):
    for y in range(w):
        if graph[x][y] == 'C':
            laser_loc.append([x, y])

visit = [[False for _ in range(w)] for _ in range(h)]

sx, sy = laser_loc[0]
ex, ey = laser_loc[1]

queue = deque()

visit[sx][sy] = True
queue.append((sx, sy, 0))

while queue:
    x, y, cnt = queue.popleft()

    if x == ex and y == ey:
        print(cnt-1)
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        while 0 <= nx < h and 0 <= ny < w and graph[nx][ny] != '*':
            if not visit[nx][ny]:
                visit[nx][ny] = True
                queue.append((nx, ny, cnt + 1))

            nx += dx[i]
            ny += dy[i]