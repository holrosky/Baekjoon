import sys

input = sys.stdin.readline

n = int(input().strip())

def add(dict, arr):
    if len(arr) == 0:
        return

    if arr[0] not in dict:
        dict[arr[0]] = {}
    add(dict[arr[0]], arr[1:])

def dfs(dict, depth):
    for i in sorted(dict.keys()):
        print('--'*depth+i)
        dfs(dict[i], depth+1)

dict = {}

for _ in range(n):
    temp = input().split()[1:]
    add(dict, temp)

dfs(dict, 0)