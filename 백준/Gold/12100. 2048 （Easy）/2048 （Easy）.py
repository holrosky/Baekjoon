import sys
from copy import deepcopy

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
input = sys.stdin.readline
n = int(input().rstrip())

board = [list(map(int, input().split())) for _ in range(n)]


answer = 0
for i in range(n):
    for j in range(n):
        answer = max(answer, board[i][j])


def dfs(depth, board):
    global answer
    if depth >= 5:
        return

    for i in range(4):
        temp_board = deepcopy(board)
        merge = [[False for _ in range(n)] for _ in range(n)]
        change = False

        if i % 2 == 0:
            start, end, step = 0, n, 1
        else:
            start, end, step = n-1, -1, -1

        for x in range(start, end, step):
            for y in range(start, end, step):
                if not temp_board[x][y]:
                    continue

                cx = x
                cy = y

                new_x = x + dx[i]
                new_y = y + dy[i]

                while True:
                    if 0 > new_x or new_x >= n or 0 > new_y or new_y >= n:
                        break

                    if temp_board[new_x][new_y]:
                        if temp_board[new_x][new_y] == temp_board[cx][cy] and not merge[new_x][new_y] and not merge[cx][cy]:
                            change = True
                            temp_board[new_x][new_y] *= 2
                            merge[new_x][new_y] = True
                            answer = max(answer, temp_board[new_x][new_y])
                            temp_board[cx][cy] = 0
                            merge[cx][cy] = False
                        else:
                            break
                    else:
                        change = True
                        temp_board[new_x][new_y] = temp_board[cx][cy]
                        temp_board[cx][cy] = 0

                        merge[new_x][new_y] = merge[cx][cy]
                        merge[cx][cy] = False
                        cx = new_x
                        cy = new_y

                    new_x += dx[i]
                    new_y += dy[i]

        if change:
            dfs(depth+1, temp_board)

dfs(0, board)

print(answer)