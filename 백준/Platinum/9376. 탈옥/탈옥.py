import sys
from collections import deque

n = int(sys.stdin.readline())

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

queue = deque()

def bfs(x, y):
    visit = [[-1 for _ in range(w)] for _ in range(h)]
    visit[x][y] = 0

    queue.append([x, y])

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < h and 0 <= ny < w:
                if visit[nx][ny] == -1:
                    if graph[nx][ny] == '#':
                        visit[nx][ny] = visit[x][y] + 1
                        queue.append([nx, ny])
                    elif graph[nx][ny] == '.':
                        visit[nx][ny] = visit[x][y]
                        queue.appendleft([nx, ny])

    return visit

for _ in range(n):
    h, w = map(int, sys.stdin.readline().split())

    graph = [['.'] + list(sys.stdin.readline().rstrip()) + ['.'] for _ in range(h)]

    graph.insert(0, ['.' for _ in range(w+2)])
    graph.append(['.' for _ in range(w + 2)])

    h = h+2
    w = w+2

    prisoner_loc = []

    for x in range(h):
        for y in range(w):
            if graph[x][y] == '$':
                prisoner_loc.append((x, y))
                graph[x][y] = '.'

    ax, ay = prisoner_loc[0]
    bx, by = prisoner_loc[1]

    a = bfs(0, 0)
    b = bfs(ax, ay)
    c = bfs(bx, by)
   
    answer = float('inf')

    for i in range(h):
        for j in range(w):
            if a[i][j] != -1 and b[i][j] != -1 and c[i][j] != -1:
                cnt = a[i][j] + b[i][j] + c[i][j]
                if graph[i][j] == '#':
                    cnt -= 2
                answer = min(answer, cnt)

    print(answer)