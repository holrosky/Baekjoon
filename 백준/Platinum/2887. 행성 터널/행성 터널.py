import sys

input = sys.stdin.readline

def find(x):
    if x == parent[x]:
        return x

    y = find(parent[x])
    parent[x] = y
    return y

def union(x, y):
    x = find(x)
    y = find(y)

    parent[x] = y


n = int(input().rstrip())

planet_x = []
planet_y = []
planet_z = []

for i in range(n):
    x, y, z = map(int, input().split())
    planet_x.append([i, x, y, z])
    planet_y.append([i, x, y, z])
    planet_z.append([i, x, y, z])

planet_x.sort(key=lambda x: x[1])
planet_y.sort(key=lambda x: x[2])
planet_z.sort(key=lambda x: x[3])

edges = []
# edge = ( distance, node1, node2 )
for i in range(len(planet_x) - 1):
    edge = (abs(planet_x[i + 1][1] - planet_x[i][1]), planet_x[i][0], planet_x[i + 1][0])
    edges.append(edge)

for i in range(len(planet_y) - 1):
    edge = (abs(planet_y[i + 1][2] - planet_y[i][2]), planet_y[i][0], planet_y[i + 1][0])
    edges.append(edge)

for i in range(len(planet_z) - 1):
    edge = (abs(planet_z[i + 1][3] - planet_z[i][3]), planet_z[i][0], planet_z[i + 1][0])
    edges.append(edge)

edges.sort()

parent = [0] * n

for i in range(n):
    parent[i] = i
    
total = 0
for edge in edges:
    dist, x, y = edge
    if find(x) != find(y):
        union(x, y)
        total += dist

print(total)