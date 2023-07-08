d = [[0 for j in range(19)] for i in range(19)]
for i in range(19):
    d[i][:] = input().split()
n = int(input())
x = []
y = []

for i in range(n):
    a, b = input().split()
    x.append(int(a) - 1)
    y.append(int(b) - 1)

for i in x:
    for j in range(19):
        if d[i][j] == "1":
            d[i][j] = "0"
        else:
            d[i][j] = "1"

for i in y:
    for j in range(19):
        if d[j][i] == "1":
            d[j][i] = "0"
        else:
            d[j][i] = "1"

for i in range(19):
    for j in range(19):
        print(d[i][j], end=" ")
    print()
