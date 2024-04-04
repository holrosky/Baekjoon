import sys
import heapq

n = int(sys.stdin.readline())

left = []
right = []

for _ in range(n):
    num = int(sys.stdin.readline())
    if len(left) == len(right):
        heapq.heappush(left, -num)
    else:
        heapq.heappush(right, num)

    if right and right[0] < -left[0]:
        a = heapq.heappop(left)
        b = heapq.heappop(right)

        heapq.heappush(left, -b)
        heapq.heappush(right, -a)

    print(-left[0])