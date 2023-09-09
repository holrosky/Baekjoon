import sys
from collections import deque

input = sys.stdin.readline

n, m  = map(int, input().split())

indegree = [0] * (n+1)
graph = [[] for _ in range(n+1)]
queue = deque()

for _ in range(m):
	a, b = map(int, input().split())
	
	indegree[b] += 1
	graph[a].append(b)
	
for i in range(1, n+1):
	if not indegree[i]:
		queue.append(i)
		
while queue:
	node = queue.popleft()
	print(node, end=' ')
	
	for each in graph[node]:
		indegree[each] -= 1
		
		if not indegree[each]:
			queue.append(each)