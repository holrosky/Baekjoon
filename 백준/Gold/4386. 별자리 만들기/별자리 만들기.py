import sys
from math import sqrt
import heapq

input = sys.stdin.readline

n = int(input().rstrip())

dist = [[] for _ in range(n)]
prim_dist = [float('inf')] * n
visit = set()
coor = []

for _ in range(n):
    x, y = map(float, input().split())
    coor.append([x, y])

for i in range(n):
    x1, y1 = coor[i]
    for j in range(i+1, n):
        x2, y2 = coor[j]
        temp = sqrt(((x2-x1)**2) + ((y2-y1)**2))
        dist[i].append((j, temp))
        dist[j].append((i, temp))

queue = []
heapq.heappush(queue, (0, 0))

min_sum = 0

while queue:
    cost, node = heapq.heappop(queue)

    if node in visit:
        continue

    visit.add(node)
    min_sum += cost

    for next_node, next_cost in dist[node]:
        heapq.heappush(queue, (next_cost, next_node))

print(round(min_sum, 2))