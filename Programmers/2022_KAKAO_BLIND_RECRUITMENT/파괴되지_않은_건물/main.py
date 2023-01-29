def solution(board, skill):
    answer = 0
    convert = {1: -1, 2: 1}
    N, M = len(board), len(board[0])
    cum = [[0 for _ in range(M + 1)] for _ in range(N + 1)]
    for typ, r1, c1, r2, c2, degree in skill:
        cum[r1][c1] += convert[typ] * degree
        cum[r1][c2 + 1] -= convert[typ] * degree
        cum[r2 + 1][c1] -= convert[typ] * degree
        cum[r2 + 1][c2 + 1] += convert[typ] * degree
    for i in range(N + 1):
        for j in range(1, M + 1):
            cum[i][j] += cum[i][j - 1]
    for i in range(1, N + 1):
        for j in range(M + 1):
            cum[i][j] += cum[i - 1][j]
    for i in range(N):
        for j in range(M):
            if 0 < board[i][j] + cum[i][j]:
                answer += 1
    return answer