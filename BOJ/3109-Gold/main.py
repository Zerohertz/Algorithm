import sys

read = sys.stdin.readline

R, C = map(int, read().split())

l = [[0 for _ in range(C)] for _ in range(R)]

for i in range(R):
    l[i] = list(read().rstrip())

vec = [-1, 0, 1]
visit = [[False for _ in range(C)] for _ in range(R)]


def DFS(i, j):
    if j == C - 1:
        return True
    for v in vec:
        if 0 <= i + v < R and l[i + v][j + 1] == "." and not visit[i + v][j + 1]:
            visit[i + v][j + 1] = True
            if DFS(i + v, j + 1):
                return True
    return False


res = 0
for i in range(R):
    if l[i][0] == ".":
        if DFS(i, 0):
            res += 1

print(res)
