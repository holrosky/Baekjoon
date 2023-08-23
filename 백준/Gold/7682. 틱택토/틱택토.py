import sys

input = sys.stdin.readline

def possible_win(win_list):
    temp = [[0 for _ in range(3)] for _ in range(3)]
    max_val = 0

    for each in win_list:
        for x, y in each:
            temp[x][y] += 1

    for x in range(3):
        for y in range(3):
            max_val = max(max_val, temp[x][y])

    if max_val == len(win_list):
        return True

    return False

while True:
    s = input().rstrip()
    board = [['' for _ in range(3)] for _ in range(3)]
    if s == 'end':
        break

    x_cnt = 0
    o_cnt = 0
    empty_cnt = 0

    x_win_list = []
    o_win_list = []

    x = y = 0

    for each in s:
        board[x][y] = each

        if each == 'X':
            x_cnt += 1
        elif each == 'O':
            o_cnt += 1
        else:
            empty_cnt += 1

        y += 1
        if y == 3:
            x += 1
            y = 0

    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2]:
            if board[i][0] == 'X':
                x_win_list.append([[i, 0], [i, 1], [i, 2]])
            elif board[i][0] == 'O':
                o_win_list.append([[i, 0], [i, 1], [i, 2]])

        if board[0][i] == board[1][i] == board[2][i]:
            if board[0][i] == 'X':
                x_win_list.append([[0, i], [1, i], [2, i]])
            elif board[0][i] == 'O':
                o_win_list.append([[0, i], [1, i], [2, i]])

    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] == 'X':
            x_win_list.append([[0, 0], [1, 1], [2, 2]])
        elif board[0][0] == 'O':
            o_win_list.append([[0, 0], [1, 1], [2, 2]])

    if board[0][2] == board[1][1] == board[2][0]:
        if board[0][2] == 'X':
            x_win_list.append([[0, 2], [1, 1], [2, 0]])
        elif board[0][2] == 'O':
            o_win_list.append([[0, 2], [1, 1], [2, 0]])

    did_x_win = False
    did_o_win = False

    if len(x_win_list):
        did_x_win = True
        if not possible_win(x_win_list):
            print('invalid')
            continue

    if len(o_win_list):
        did_o_win = True
        if not possible_win(o_win_list):
            print('invalid')
            continue

    if o_cnt > x_cnt:
        print('invalid')
        continue

    if did_o_win and did_x_win:
        print('invalid')
        continue

    if did_x_win and (x_cnt - o_cnt != 1):
        print('invalid')
        continue

    if did_o_win and (x_cnt != o_cnt):
        print('invalid')
        continue

    if not did_o_win and not did_x_win and empty_cnt:
        print('invalid')
        continue

    print('valid')