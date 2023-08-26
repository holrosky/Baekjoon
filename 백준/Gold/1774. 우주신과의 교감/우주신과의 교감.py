import sys
import heapq
from math import sqrt

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n)]
coor = []

pre_conn = set()
visit = set()

for _ in range(n):
    x, y = map(int, input().split())
    coor.append([x, y])

for _ in range(m):
    x, y = map(int, input().split())
    pre_conn.add((x-1, y-1))
    pre_conn.add((y-1, x-1))

for i in range(n):
    x1, y1 = coor[i]
    for j in range(i+1, n):
        x2, y2 = coor[j]
        temp = 0 if (i, j) in pre_conn or (j, i) in pre_conn else sqrt(((x2-x1)**2) + ((y2-y1)**2))
        graph[i].append((j, temp))
        graph[j].append((i, temp))


queue = []
heapq.heappush(queue, (0, 0))

min_val = 0

while queue:
    cost, node = heapq.heappop(queue)

    if node in visit:
        continue

    visit.add(node)
    min_val += cost

    for next_node, next_cost in graph[node]:
        heapq.heappush(queue, (next_cost, next_node))

print("{:.2f}".format(round(min_val, 2)))