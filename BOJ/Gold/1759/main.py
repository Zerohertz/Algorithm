import sys
from itertools import combinations

read = sys.stdin.readline

L, C = map(int, read().split())
S = sorted(map(str, read().split()))

moum = set('aeiou')

for i in combinations(S, L):
    cntmoum = 0
    cntjaum = 0
    for tmp in i:
        if tmp in moum:
            cntmoum += 1
        else:
            cntjaum += 1
    if cntmoum >= 1 and cntjaum >= 2:
        print(''.join(i))
