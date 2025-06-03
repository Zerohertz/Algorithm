N = int(input())

L = []

for i in range(N):
    L.append(input())

l = []

for i in set(L):
    l.append([i, len(i)])

l.sort(key=lambda x: (x[1], x[0]))

for i in range(len(l)):
    print(l[i][0])
