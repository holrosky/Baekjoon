import sys

n, k = map(int, sys.stdin.readline().split())
gems = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dp = [0] * (k+1)

for w,v in gems:
    for i in range(k, w-1, -1):
        dp[i] = max(dp[i], dp[i - w] + v)

print(max(dp))