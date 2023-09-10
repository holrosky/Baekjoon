import sys
from collections import deque

input = sys.stdin.readline

tc = int(input().strip())

for _ in range(tc):
    n = int(input().strip())

    nodes = list(map(int, input().split()))
    m = int(input().strip())

    graph = [set() for _ in range(n+1)]

    for i in range(n):
        for j in range(i+1, n):
            graph[nodes[i]].add(nodes[j])

    indegree = [n-(len(x)+1) for x in graph]


    for _ in range(m):
        a, b = map(int, input().split())
        if a in graph[b]:
            graph[a].add(b)
            graph[b].remove(a)

            indegree[a] -= 1
            indegree[b] += 1
        else:
            graph[b].add(a)
            graph[a].remove(b)

            indegree[b] -= 1
            indegree[a] += 1

    queue = deque()

    error = False

    cnt = 0
    for i in range(1, n+1):
        if not indegree[i]:
            cnt += 1
            queue.append(i)

            if cnt >= 2:
                error = True
                break

        if error:
            break

    if error:
        print('?')
        continue

    error = False
    res = []
    while queue:
        node = queue.popleft()
        res.append(str(node))

        cnt = 0
        for each in graph[node]:
            indegree[each] -= 1

            if not indegree[each]:
                cnt += 1
                queue.append(each)

        if cnt >= 2:
            error = True
            break

    if error:
        print('?')
    elif not res or len(res) < n:
        print('IMPOSSIBLE')
    else:
        print(' '.join(res))