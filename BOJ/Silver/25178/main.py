import sys
from collections import Counter

read = sys.stdin.readline

N = int(read())
A = str(read().rstrip())
B = str(read().rstrip())
moum = ('a', 'e', 'i', 'o', 'u')

cA = Counter(A)
cB = Counter(B)

if cA == cB and A[0] == B[0] and A[-1] == B[-1]:
    for i in moum:
        A = A.replace(i, '')
        B = B.replace(i, '')
    if A == B:
        print('YES')
    else:
        print('NO')
else:
    print('NO')
