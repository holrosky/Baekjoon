import sys
input = sys.stdin.readline

pattern = input().replace('\n', '')

ans = 0

for a in range(len(pattern)):
    sub_pattern = pattern[a:]
    i = 0
    table = [0] * len(sub_pattern)

    for j in range(1, len(sub_pattern)):
        while i > 0 and sub_pattern[i] != sub_pattern[j]:
            i = table[i-1]

        if sub_pattern[i] == sub_pattern[j]:
            i += 1
            table[j] = i

    ans = max(ans, max(table))

print(ans)