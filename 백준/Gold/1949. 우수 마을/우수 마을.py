import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n = int(input().rstrip())
edges = [[] for _ in range(n + 1)]

resident = [0] + list(map(int, input().split()))

dp = [[0, 0] for _ in range(n + 1)]
visit = set()

for _ in range(n - 1):
    u, v = map(int, input().split())
    edges[u].append(v)
    edges[v].append(u)


def dfs(node):

    dp[node][0] = 0
    dp[node][1] = resident[node]

    x = 0
    y = 0

    for child in edges[node]:
        if child not in visit:
            visit.add(child)
            a, b = dfs(child)
            x += max(a, b)
            y += a

    dp[node][0] += x
    dp[node][1] += y

    return dp[node][0], dp[node][1]

visit.add(1)
dfs(1)

print(max(dp[1][0], dp[1][1]))