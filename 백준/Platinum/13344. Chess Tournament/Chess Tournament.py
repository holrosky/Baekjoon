import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())

parent = [i for i in range(n)]
compares = []
group = set()
graph = [[] for _ in range(n)]
inDgree = {}

def find(x):
    if parent[x] == x:
        return x

    y = find(parent[x])
    parent[x] = y
    return y

def union(x, y):
    x = find(parent[x])
    y = find(parent[y])

    parent[y] = x

for _ in range(m):
    k, s, l = input().split()

    if s == '=':
        union(int(k), int(l))
    else:
        compares.append([int(k), int(l)])


for each in parent:
    group.add(find(each))

for k, l in compares:
    x = find(k)
    y = find(l)

    if x == y:
        print('inconsistent')
        break

    graph[x].append(y)
    if x not in inDgree:
        inDgree[x] = 0
    if y not in inDgree:
        inDgree[y] = 0

    inDgree[y] += 1

else:
    queue = deque()

    for k, v in inDgree.items():
        if v == 0:
            queue.append(k)

    while queue:
        g = queue.popleft()

        for each in graph[g]:
            inDgree[each] -= 1

            if inDgree[each] == 0:
                queue.append(each)

    for k, v in inDgree.items():
        if v:
            print('inconsistent')
            break
    else:
        print('consistent')