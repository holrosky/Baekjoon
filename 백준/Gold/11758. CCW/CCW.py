import sys
input = sys.stdin.readline

coor = []

for _ in range(3):
    x, y = map(int, input().split())
    coor.append([x, y])

ccw = ((coor[0][0]*coor[1][1] + coor[1][0]*coor[2][1] + coor[2][0]*coor[0][1]) - (coor[1][0]*coor[0][1] + coor[2][0]*coor[1][1] + coor[0][0]*coor[2][1]))

if ccw > 0:
    print(1)
elif ccw == 0:
    print(0)
else:
    print(-1)