import sys

input = sys.stdin.readline
n, l = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]
res = 0

for _ in range(2):
    for x in range(n):
        installed = [False] * n
        sorted_list = sorted([(val, idx) for idx, val in enumerate(graph[x])])

        while sorted_list:
            val, idx = sorted_list.pop()

            left_flag = False
            right_flag = False

            if idx != 0:
                for i in range(1, l+1):
                    if idx-i < 0:
                        left_flag = True
                        break

                    if graph[x][idx-i] > val:
                        break

                    if graph[x][idx-i] == val and i == 1:
                        break

                    if graph[x][idx-1] != val-1 or installed[idx-i]:
                        left_flag = True
                        break

                else:
                    for i in range(1, l + 1):
                        installed[idx - i] = True

            if idx != n-1:
                for i in range(1, l + 1):
                    if idx + i >= n:
                        right_flag = True
                        break

                    if graph[x][idx + i] > val:
                        break

                    if graph[x][idx + i] == val and i == 1:
                        break

                    if graph[x][idx + 1] != val - 1 or installed[idx + i]:
                        right_flag = True
                        break

                else:
                    for i in range(1, l + 1):
                        installed[idx+i] = True

            if left_flag or right_flag:
                break


        else:
            res += 1

    graph = [list(x) for x in zip(*graph)]

print(res)