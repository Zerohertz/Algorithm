M = int(input())
ncard = list(map(int, input().split()))
ndict = dict()
for i in ncard:
    if i in ndict:
        ndict[i] += 1
    else:
        ndict[i] = 1

N = int(input())
scard = list(map(int, input().split()))

for i in scard:
    if i in ndict:
        print(ndict[i], end=" ")
    else:
        print(0, end=" ")
