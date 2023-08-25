import sys
import heapq

tc = int(sys.stdin.readline().rstrip())

for _ in range(tc):
	n, d, c = map(int, sys.stdin.readline().split())
	
	graph = [[] for _ in range(n+1)]
	dist = [float('inf')] * (n+1)
	dist[c] = 0
	queue = []
	heapq.heappush(queue, (0, c))
	
	for _ in range(d):
		a, b, s = map(int, sys.stdin.readline().split())
		graph[b].append([a, s])
	
	while queue:
		cost, node = heapq.heappop(queue)
		
		if cost > dist[node]:
			continue
			
		for next_node, next_cost in graph[node]:
			new_dist = cost + next_cost
			if new_dist < dist[next_node]:
				dist[next_node] = new_dist
				heapq.heappush(queue, (new_dist, next_node))
				
	inf_cnt = 0
	need_time = 0
	
	for i in range(1, n+1):
		if dist[i] != float('inf'):
			inf_cnt += 1
			need_time = max(need_time, dist[i])
			
	print(f'{inf_cnt} {need_time}')