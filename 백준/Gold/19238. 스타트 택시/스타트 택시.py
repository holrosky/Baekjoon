import sys
from collections import deque

input = sys.stdin.readline

answer = 0

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

n, m, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
x, y = map(int, input().split())

queue = deque()
visit = [[False for _ in range(n)] for _ in range(n)]
queue.append((x-1, y-1, 0))

dest_pair = {}

for _ in range(m):
    a, b, c, d = map(int, input().split())
    dest_pair[(a-1, b-1)] = (c-1, d-1)

shortest_cost = float('inf')
closest_coor = (n, m)
can_take = False

while True:
    while queue and dest_pair:
        cx, cy, cnt = queue.popleft()

        if (cx, cy) in dest_pair:
            if cnt <= shortest_cost:
                shortest_cost = cnt
                if cx < closest_coor[0] or (cx == closest_coor[0] and cy < closest_coor[1]):
                    closest_coor = (cx, cy)

                can_take = True

        else:
            for i in range(4):
                nx = cx + dx[i]
                ny = cy + dy[i]

                if 0 <= nx < n and 0 <= ny < n and not graph[nx][ny] and not visit[nx][ny] and cnt < shortest_cost:
                    queue.append((nx, ny, cnt+1))
                    visit[nx][ny] = True

    if can_take:
        px, py = closest_coor
        ex, ey = dest_pair[closest_coor]

        from_p_to_e = -1

        queue = deque()
        visit = [[False for _ in range(n)] for _ in range(n)]

        queue.append((px, py, 0))

        while queue:
            cx, cy, cnt = queue.popleft()

            if cx == ex and cy == ey:
                from_p_to_e = cnt
                break

            else:
                for i in range(4):
                    nx = cx + dx[i]
                    ny = cy + dy[i]

                    if 0 <= nx < n and 0 <= ny < n and not graph[nx][ny] and not visit[nx][ny]:
                        queue.append((nx, ny, cnt + 1))
                        visit[nx][ny] = True

        if from_p_to_e == -1:
            break

        total_fuel_needed = shortest_cost + from_p_to_e

        if total_fuel_needed > k:
            break

        k = k - total_fuel_needed + (2 * from_p_to_e)

        del(dest_pair[closest_coor])

        if not dest_pair:
            break

        queue = deque()
        visit = [[False for _ in range(n)] for _ in range(n)]

        queue.append((ex, ey, 0))
        closest_coor = (n, n)
        can_take = False
        shortest_cost = float('inf')
    else:
        break

if not dest_pair:
    print(k)
else:
    print(-1)