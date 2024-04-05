import sys
from collections import deque

dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

r, c = map(int, sys.stdin.readline().split())

cave = [list(sys.stdin.readline().rstrip()) for _ in range(r)]

_ = sys.stdin.readline()
throws = list(map(int, sys.stdin.readline().split()))

left_turn = True


def destroy_mineral(row):
    if left_turn:
        for i in range(c):
            if cave[r - row][i] == 'x':
                cave[r - row][i] = '.'
                break
    else:
        for i in range(c - 1, -1, -1):
            if cave[r - row][i] == 'x':
                cave[r - row][i] = '.'
                break


def find_cluster(floor=True, rin=None, cin=None):
    cluster_coor = set()
    queue = deque()

    if floor:
        for i in range(c):
            if cave[r - 1][i] == 'x':
                queue.append((r - 1, i))
                cluster_coor.add((r - 1, i))
    else:
        queue.append((rin, cin))
        cluster_coor.add((rin, cin))

    while queue:
        cr, cc = queue.popleft()

        for i in range(4):
            new_r = cr + dr[i]
            new_c = cc + dc[i]

            if 0 <= new_r < r and 0 <= new_c < c and cave[new_r][new_c] == 'x' and (new_r, new_c) not in cluster_coor:
                cluster_coor.add((new_r, new_c))
                queue.append((new_r, new_c))

    return cluster_coor


def get_move_offset(floor_cluster_coor, drop_cluster_coor):
    move_offset = 1

    while True:
        for row, col in drop_cluster_coor:
            if (row+move_offset, col) in floor_cluster_coor:
                return move_offset-1

        for row, col in drop_cluster_coor:
            if row+move_offset == r-1:
                return move_offset
        move_offset += 1

def move_down(floor_cluster_coor):
    for i in range(r):
        for j in range(c):
            if (i, j) not in floor_cluster_coor and cave[i][j] == 'x':
                cluster_coor = find_cluster(False, i, j)
                move_offset = get_move_offset(floor_cluster_coor, cluster_coor)

                for coor_r, coor_c in cluster_coor:
                    cave[coor_r][coor_c] = '.'
                    
                for coor_r, coor_c in cluster_coor:
                    cave[coor_r + move_offset][coor_c] = 'x'

                return


for row in throws:
    destroy_mineral(row)
    move_down(find_cluster())
    left_turn = not left_turn

for row in cave:
    print(''.join(row))
