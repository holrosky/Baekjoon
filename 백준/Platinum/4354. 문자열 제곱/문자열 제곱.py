import sys
input = sys.stdin.readline

while True:
    s = input().strip()

    if s == '.':
        break

    table = [0] * len(s)
    i = 0

    for j in range(1, len(s)):
        while i > 0 and s[i] != s[j]:
            i = table[i-1]

        if s[i] == s[j]:
            i += 1
            table[j] = i

    if len(s) % (len(s) - table[-1]) != 0:
        print(1)
    else:
        print(len(s) // (len(s) - table[-1]))