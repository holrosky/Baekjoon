import sys
from collections import deque

input = sys.stdin.readline

answer = 0

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

loc = {}
dir = {}

dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]

isolate = set()
done = False

convert_dir = [0, 2, 1, 4, 3]

n, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
state_map = [[[] for _ in range(n)] for _ in range(n)]

turn_cnt = 0

for i in range(k):
    x, y, d = map(int, input().split())

    loc[i] = (x-1, y-1)
    dir[i] = d
    state_map[x-1][y-1].append(i)

while True:
    if turn_cnt > 1000:
        break

    for i in range(k):
        x, y = loc[i]
        d = dir[i]

        nx = x + dx[d]
        ny = y + dy[d]

        index = None

        for idx, val in enumerate(state_map[x][y]):
            if val == i:
                index = idx
                break

        if not 0 <= nx < n or not 0 <= ny < n:
            d = convert_dir[d]
            dir[i] = d

            nx = x + dx[d]
            ny = y + dy[d]

            if graph[nx][ny] == 2:
                dir[i] = d

        if graph[nx][ny] == 0:
            temp = state_map[x][y][index:]
            state_map[nx][ny] += temp

            for each in temp:
                loc[each] = (nx, ny)

            state_map[x][y] = state_map[x][y][:index]

            if len(state_map[nx][ny]) >= 4:
                done = True
                break

        elif graph[nx][ny] == 1:
            temp = state_map[x][y][index:]
            state_map[nx][ny] += temp[::-1]

            for each in temp:
                loc[each] = (nx, ny)

            state_map[x][y] = state_map[x][y][:index]

            if len(state_map[nx][ny]) >= 4:
                done = True
                break

        elif graph[nx][ny] == 2:
            d = convert_dir[d]
            dir[i] = d

            nx = x + dx[d]
            ny = y + dy[d]

            if (not 0 <= nx < n or not 0 <= ny < n) or graph[nx][ny] == 2:
                dir[i] = d

            elif graph[nx][ny] == 0:
                temp = state_map[x][y][index:]
                state_map[nx][ny] += temp

                for each in temp:
                    loc[each] = (nx, ny)

                state_map[x][y] = state_map[x][y][:index]

                if len(state_map[nx][ny]) >= 4:
                    done = True
                    break

            elif graph[nx][ny] == 1:
                temp = state_map[x][y][index:]
                state_map[nx][ny] += temp[::-1]

                for each in temp:
                    loc[each] = (nx, ny)

                state_map[x][y] = state_map[x][y][:index]

                if len(state_map[nx][ny]) >= 4:
                    done = True
                    break
    turn_cnt += 1

    if done:
        break

if not done:
    print(-1)
else:
    print(turn_cnt)