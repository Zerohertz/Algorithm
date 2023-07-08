n = int(input())
x = []
y = []

for i in range(n):
    a, b = input().split()
    x.append(int(a) - 1)
    y.append(int(b) - 1)

d = [[0 for j in range(19)] for i in range(19)]

for i in range(n):
    d[x[i]][y[i]] = 1

for i in range(19):
    for j in range(19):
        print(d[i][j], end=" ")
    print()
