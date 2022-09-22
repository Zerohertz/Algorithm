def printer(l):
    dupl = [i for i in l]
    dupl.sort(key=lambda x: x[0])
    M = dupl[-1][0]
    m = dupl[0][0]
    if l[0] == M or M == m:
        return l
    while M != l[0][0]:
        l.append(l[0])
        del l[0]
    return l


import sys

read = sys.stdin.readline

T = int(read())

for _ in range(T):
    N, M = map(int, read().split())
    l = list(map(int, read().split()))
    lidx = [[l[i], i] for i in range(N)]
    cnt = 1
    for i in range(N):
        printer(lidx)
        if lidx[0][1] == M:
            print(cnt)
            break
        else:
            del lidx[0]
            cnt += 1