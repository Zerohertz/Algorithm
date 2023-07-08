def convertMatrix(stickInfo, matrix):
    if stickInfo[1] == "0":
        for i in range(int(stickInfo[0])):
            matrix[int(stickInfo[2]) - 1][int(stickInfo[3]) - 1 + i] = "1"
    elif stickInfo[1] == "1":
        for i in range(int(stickInfo[0])):
            matrix[int(stickInfo[2]) - 1 + i][int(stickInfo[3]) - 1] = "1"
    return matrix


a, b = input().split()
a = int(a)
b = int(b)
d = [[0 for j in range(b)] for i in range(a)]
n = int(input())
sticks = [[0 for j in range(4)] for i in range(n)]
for i in range(n):
    sticks[i][:] = input().split()
for i in range(n):
    d = convertMatrix(sticks[:][i], d)
for i in range(a):
    for j in range(b):
        print(d[i][j], end=" ")
    print()
