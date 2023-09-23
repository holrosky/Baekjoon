import sys

input = sys.stdin.readline
n, m, x, y, k = map(int, input().split())

dice = {}

for i in range(6):
    dice[i] = 0

dir = [[], [2, 3, 1, 0, 4, 5],
       [3, 2, 0, 1, 4, 5],
       [5, 4, 2, 3, 0, 1],
       [4, 5, 2, 3, 1, 0]]

dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]

board = [list(map(int, input().split())) for _ in range(n)]
commands = list(map(int, input().split()))

for command in commands:
    new_x = x + dx[command]
    new_y = y + dy[command]
    
    if 0 <= new_x < n and 0 <= new_y < m:
        temp_dice = {}

        for idx, val in enumerate(dir[command]):
            temp_dice[val] = dice[idx]

        print(temp_dice[0])

        if board[new_x][new_y]:
            temp_dice[1] = board[new_x][new_y]
            board[new_x][new_y] = 0
        else:
            board[new_x][new_y] = temp_dice[1]

        x += dx[command]
        y += dy[command]

        dice = temp_dice