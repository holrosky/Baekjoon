import sys
input = sys.stdin.readline

text = input().replace('\n', '')
pattern = input().replace('\n', '')

i = 0
table = [0] * len(pattern)

for j in range(1, len(pattern)):
    while i > 0 and pattern[i] != pattern[j]:
        i = table[i-1]

    if pattern[i] == pattern[j]:
        i += 1
        table[j] = i

result = []

i = 0

for j in range(len(text)):
    while i > 0 and pattern[i] != text[j]:
        i = table[i-1]

    if pattern[i] == text[j]:
        i += 1

        if i == len(pattern):
            result.append(str(j-i+2))
            i = table[i-1]

print(len(result))
print(' '.join(result))