import sys

read = sys.stdin.readline

N = int(read())
l = [0 for _ in range(26)]

for i in range(N):
    tmp = read().rstrip()
    for j, k in enumerate(tmp[::-1]):
        l[ord(k) - ord('A')] += 10 ** j

l.sort(reverse=True)

res = 0
tmp = 9
for i in l[:9]:
    res += i * tmp
    tmp -= 1

print(res)
