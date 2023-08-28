import sys
sys.setrecursionlimit(10**9)

input = sys.stdin.readline

n, r, q = map(int, input().split())

graph = [[] for _ in range(n+1)]
num_of_nodes = [0] * (n+1)

visit = set()

for _ in range(n-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(root):
    visit.add(root)
    num_of_children = 1

    for child in graph[root]:
        if child not in visit:
            visit.add(child)
            num_of_children += dfs(child)

    num_of_nodes[root] = num_of_children
    return num_of_children

dfs(r)

for _ in range(q):
    query = int(input().rstrip())
    print(num_of_nodes[query])
