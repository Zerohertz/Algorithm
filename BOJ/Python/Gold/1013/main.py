import re
import sys

read = sys.stdin.readline

T = int(read())
for _ in range(T):
    S = read().strip()
    p = re.compile("(100+1+|01)+")
    res = p.fullmatch(S)
    if res:
        print("YES")
    else:
        print("NO")
