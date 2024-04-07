import sys

while True:
    histogram = list(map(int, sys.stdin.readline().split()))
    n = histogram[0]

    if n == 0:
        break

    stack = []
    max_area = 0

    for index, height in enumerate(histogram[1:]):
        index += 1
        if not stack:
            stack.append((index, height))
            continue

        while stack and stack[-1][1] > height:
            a, b = stack.pop()
            width = index - 1 if not stack else index - stack[-1][0] - 1
            max_area = max(max_area, b * width)

        stack.append((index, height))
    while stack:
        a, b = stack.pop()
        width = n
        if stack:
            width -= stack[-1][0]
        max_area = max(max_area, b * width)

    print(max_area)