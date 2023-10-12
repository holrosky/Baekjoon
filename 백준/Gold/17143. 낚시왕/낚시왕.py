import sys
input = sys.stdin.readline

answer = 0
current_loc = 0

r, c, m = map(int, input().split())

graph = [[0 for _ in range(c)] for _ in range(r)]
shark_dict = {}

for _ in range(m):
    x, y, s, d, z = map(int, input().split())
    x -= 1
    y -= 1

    graph[x][y] = 1
    shark_dict[(x, y)] = (x, y, s, d, z)

while current_loc < c:
    for i in range(r):
        if graph[i][current_loc]:
            _, _, _, _, z = shark_dict[(i, current_loc)]
            del(shark_dict[(i, current_loc)])
            answer += z
            break

    temp = {}

    for shark in shark_dict.values():
        x, y, s, d, z = shark
        temp_s = s

        if d == 1 or d == 2:
            temp_s += r - 1 - x if d == 1 else x

            a, b = divmod(temp_s, r - 1)

            if a % 2 == 0:
                x = 0 if d == 2 else r - 1
            else:
                x = r - 1 if d == 2 else 0

            if x:
                x -= b
                d = 1
            else:
                x = b
                d = 2

        elif d == 3 or d == 4:
            temp_s += c - 1 - y if d == 4 else y

            a, b = divmod(temp_s, c - 1)

            if a % 2 == 0:
                y = 0 if d == 3 else c - 1
            else:
                y = c - 1 if d == 3 else 0

            if y:
                y -= b
                d = 4
            else:
                y = b
                d = 3

        if (x, y) not in temp:
            temp[(x, y)] = (x, y, s, d, z)
        else:
            if z > temp[(x, y)][4]:
                temp[(x, y)] = (x, y, s, d, z)

    graph = [[0 for _ in range(c)] for _ in range(r)]
    shark_dict = {}

    for shark in temp.values():
        x, y, s, d, z = shark

        graph[x][y] = 1
        shark_dict[(x, y)] = (x, y, s, d, z)

    current_loc += 1

print(answer)