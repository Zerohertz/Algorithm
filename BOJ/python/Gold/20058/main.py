import sys
from collections import deque

read = sys.stdin.readline

dx = (1, 0, -1, 0)
dy = (0, 1, 0, -1)


def simulation(board, l, L):
    new_board = [[0] * l for _ in range(l)]
    r_size = 2**L
    for y in range(0, l, r_size):
        for x in range(0, l, r_size):
            for i in range(r_size):
                for j in range(r_size):
                    new_board[y + j][x + r_size - i - 1] = board[y + i][x + j]
    board = new_board
    melting_list = []
    for y in range(l):
        for x in range(l):
            ice_count = 0
            for d in range(len(dy)):
                ny = y + dy[d]
                nx = x + dx[d]
                if nx < 0 or ny < 0 or nx >= l or ny >= l:
                    continue
                elif board[ny][nx] > 0:
                    ice_count += 1
            if ice_count < 3 and board[y][x] != 0:
                melting_list.append((y, x))
    for y, x in melting_list:
        board[y][x] -= 1
    return board


def BFS(board, l):
    used = [[False] * l for _ in range(l)]
    ice_sum = 0
    max_area_count = 0
    for y in range(l):
        for x in range(l):
            area_count = 0
            if used[y][x] or board[y][x] == 0:
                continue
            q = deque()
            q.append((y, x))
            used[y][x] = True
            while q:
                sy, sx = q.popleft()
                ice_sum += board[sy][sx]
                area_count += 1
                for d in range(4):
                    ny = sy + dy[d]
                    nx = sx + dx[d]
                    if nx < 0 or ny < 0 or nx >= l or ny >= l or used[ny][nx]:
                        continue
                    if board[ny][nx] != 0:
                        used[ny][nx] = True
                        q.append((ny, nx))
            max_area_count = max(max_area_count, area_count)
    print(ice_sum)
    print(max_area_count)


N, Q = map(int, read().split())
l = 2**N
board = [list(map(int, read().split())) for _ in range(l)]
sim = list(map(int, read().split()))
for L in sim:
    board = simulation(board, l, L)
BFS(board, l)
