import sys

def solution(n, s, a, b, fares):
    answer = sys.maxsize
    s -= 1
    a -= 1
    b -= 1
    l = [[sys.maxsize for _ in range(n)] for _ in range(n)]
    for p1, p2, f in fares:
        l[p1 - 1][p2 - 1] = f
        l[p2 - 1][p1 - 1] = f
    for k in range(n):
        for i in range(n):
            for j in range(n):
                l[i][j] = min(l[i][j], l[i][k] + l[k][j])
    for i in range(n):
        if i == a:
            answer = min(answer, l[s][a] + l[a][b])
        elif i == b:
            answer = min(answer, l[s][b] + l[b][a])
        else:
            answer = min(answer, l[s][i] + l[i][a] + l[i][b])
    answer = min(answer, l[s][a] + l[s][b])
    return answer