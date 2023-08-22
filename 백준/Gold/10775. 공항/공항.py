import sys
sys.setrecursionlimit(10**9)

g = int(sys.stdin.readline().rstrip())
p = int(sys.stdin.readline().rstrip())

count = 0

plane_list = []
for i in range(p):
    plane_list.append(int(sys.stdin.readline().rstrip()))

parent = [i for i in range(g+1)]

def find(plane):
    if parent[plane] == plane:
        return plane
    
    y = find(parent[plane])
    parent[plane] = y
    return y

for plane in plane_list:
    temp = find(plane)
    if temp == 0:
        break
    parent[temp] = parent[temp-1]
    count += 1

print(count)