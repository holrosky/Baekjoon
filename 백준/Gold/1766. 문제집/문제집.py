import heapq
import sys

input = sys.stdin.readline
n, m = map(int, input().split())

inDegree = [0 for _ in range(n+1)]
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())

    inDegree[b] += 1
    graph[a].append(b)

queue = []

for i in range(1, len(inDegree)):
    if not inDegree[i]:
        heapq.heappush(queue, i)

while queue:
    question = heapq.heappop(queue)
    print(question, end= ' ')

    for i in graph[question]:
        inDegree[i] -= 1

        if not inDegree[i]:
            heapq.heappush(queue, i)
