import sys
input = sys.stdin.readline

n = int(input().strip())

text = [0] * 360000
pattern = [0] * 360000

for i in map(int, input().split()):
    text[i] += 1

for i in map(int, input().split()):
    pattern[i] += 1

text = text+text

i = 0
table = [0] * len(pattern)

for j in range(1, len(pattern)):
    while i > 0 and pattern[i] != pattern[j]:
        i = table[i-1]

    if pattern[i] == pattern[j]:
        i += 1
        table[j] = i

i = 0
result = []

for j in range(len(text)):
    while i > 0 and pattern[i] != text[j]:
        i = table[i-1]

    if pattern[i] == text[j]:
        i += 1

        if i == len(pattern):
            print('possible')
            break

else:
    print('impossible')