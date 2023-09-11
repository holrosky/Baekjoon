from collections import deque

for _ in range(int(input())):
    n, k = map(int, input().split())
    cost = [0] + list(map(int, input().split()))
    link = [[] for _ in range(n + 1)]
    cntLink = [-1] + [0] * (n)
    for _ in range(k):
        a, b = map(int, input().split())
        link[a].append(b)
        cntLink[b] += 1
    end = int(input())

    dp = [0] * (n + 1)
    q = deque()
    for i in range(1, n + 1):
        if cntLink[i] == 0:
            q.append(i)
            dp[i] = cost[i]

    while q:
        curNode = q.popleft()
        for toNode in link[curNode]:
            cntLink[toNode] -= 1
            dp[toNode] = max(dp[toNode], dp[curNode] + cost[toNode])
            if cntLink[toNode] == 0:
                q.append(toNode)

        if cntLink[end] == 0:
            print(dp[end])
            break