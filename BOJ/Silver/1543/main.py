import sys

read = sys.stdin.readline

s1 = read().rstrip()
s2 = read().rstrip()
cnt = 0
tmp = 0

while tmp <= len(s1) - len(s2):
    if s1[tmp:tmp + len(s2)] == s2:
        cnt += 1
        tmp += len(s2)
    else:
        tmp += 1

print(cnt)
