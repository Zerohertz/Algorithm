import sys
from collections import Counter

s = sorted(map(str, sys.stdin.readline().rstrip()))
c = Counter(s)
cnt = 0
mid = ''
res = ''

for i in c:
    if c[i] % 2 != 0:
        cnt += 1
        mid += i
        s.remove(i)
    if cnt > 1:
        print("I'm Sorry Hansoo")
        exit(0)

for i in range(0, len(s), 2):
    res += s[i]

print(res + mid + res[::-1])
