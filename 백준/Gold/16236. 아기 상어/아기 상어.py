import sys
from collections import deque

input = sys.stdin.readline

answer = 0

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

n = int(input().strip())

graph = [list(map(int, input().split())) for _ in range(n)]
visit = [[False for _ in range(n)] for _ in range(n)]

queue = deque()
max_cnt = float('inf')
closest_coor = (n, n)
can_eat = False
stack = 0
size = 2

for x in range(n):
    for y in range(n):
        if graph[x][y] == 9:
            queue.append((x, y, 0))
            graph[x][y] = 0
            visit[x][y] = True

while True:
    while queue:
        cx, cy, cnt = queue.popleft()

        if 0 < graph[cx][cy] < size:
            if cnt <= max_cnt:
                max_cnt = cnt
                if cx < closest_coor[0] or (cx == closest_coor[0] and cy < closest_coor[1]):
                    closest_coor = (cx, cy)

                can_eat = True

        else:
            for i in range(4):
                nx = cx + dx[i]
                ny = cy + dy[i]

                if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] <= size and not visit[nx][ny] and cnt < max_cnt:
                    queue.append((nx, ny, cnt+1))
                    visit[nx][ny] = True

    if can_eat:
        answer += max_cnt

        stack += 1
        if stack == size:
            size += 1
            stack = 0

        queue = deque()
        graph[closest_coor[0]][closest_coor[1]] = 0
        visit = [[False for _ in range(n)] for _ in range(n)]

        queue.append((closest_coor[0], closest_coor[1], 0))

        closest_coor = (n, n)
        can_eat = False
        max_cnt = float('inf')
    else:
        break

print(answer)