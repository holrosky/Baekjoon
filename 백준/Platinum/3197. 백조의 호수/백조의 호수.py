import sys
from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

r, c = map(int, sys.stdin.readline().split())
maps = [list(sys.stdin.readline().rstrip()) for _ in range(r)]

water_queue = deque()
swan_queue = deque()
temp_water_queue = deque()
temp_swan_queue = deque()

water_visit = set()
swan_visit = set()
swan_coors = []

for i in range(r):
    for j in range(c):
        if (maps[i][j] == '.') or (maps[i][j] == 'L'):
            if maps[i][j] == 'L':
                swan_coors.append([i, j])
            maps[i][j] = '.'
            water_queue.append((i, j))
            water_visit.add((i, j))

swan_queue.append((swan_coors[0][0], swan_coors[0][1]))
swan_visit.add((swan_coors[0][0], swan_coors[0][1]))

day = 0
flag = True

while flag:
    while water_queue:
        x, y = water_queue.popleft()

        maps[x][y] = '.'

        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]

            if 0 <= new_x < r and 0 <= new_y < c and maps[new_x][new_y] == 'X' and (new_x, new_y) not in water_visit:
                water_visit.add((new_x, new_y))
                temp_water_queue.append((new_x, new_y))

    while swan_queue:
        x, y = swan_queue.popleft()

        if x == swan_coors[1][0] and y == swan_coors[1][1]:
            print(day)
            flag = False
            break

        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]

            if 0 <= new_x < r and 0 <= new_y < c and (new_x, new_y) not in swan_visit:
                swan_visit.add((new_x, new_y))
                if maps[new_x][new_y] == '.' :
                    swan_queue.append((new_x, new_y))
                else:
                    temp_swan_queue.append((new_x, new_y))

    water_queue = temp_water_queue
    swan_queue = temp_swan_queue

    temp_water_queue = deque()
    temp_swan_queue = deque()

    day += 1