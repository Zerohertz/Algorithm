import sys


def convert_func(rot, s1, s2, idx_i_1, idx_j_1, idx_i_2, idx_j_2, i, j):
    if rot == 0:
        ni, nj = i + idx_i_1 - s1, j + idx_j_1 - s2
    elif rot == 1:
        ni, nj = -j + idx_i_2 + s1, i + idx_j_1 - s2
    elif rot == 2:
        ni, nj = -i + idx_i_2 + s1, -j + idx_j_2 + s2
    elif rot == 3:
        ni, nj = j + idx_i_1 - s1, -i + idx_j_2 + s2
    return ni, nj


def match(
    rot, key, M, lock, N, s1, s2, idx_i, idx_j, idx_i_1, idx_j_1, idx_i_2, idx_j_2
):
    for i in range(M):
        for j in range(M):
            ni, nj = convert_func(
                rot, s1, s2, idx_i_1, idx_j_1, idx_i_2, idx_j_2, i, j)
            if (0 <= ni < N) and (0 <= nj < N):
                if (idx_i_1 <= ni <= idx_i_2) and (idx_j_1 <= nj <= idx_j_2):
                    if key[i][j] == lock[ni][nj]:
                        return False
                    else:
                        continue
                else:
                    if key[i][j] == 1:
                        return False
                    else:
                        continue
            else:
                continue
    return True


def solution(key, lock):
    N, M = len(lock), len(key)
    idx_i_1, idx_j_1, idx_i_2, idx_j_2 = sys.maxsize, sys.maxsize, 0, 0
    for i in range(N):
        for j in range(N):
            if lock[i][j] == 0:
                idx_i_1 = min(idx_i_1, i)
                idx_j_1 = min(idx_j_1, j)
                idx_i_2 = max(idx_i_2, i)
                idx_j_2 = max(idx_j_2, j)
    if idx_i_1 == sys.maxsize:
        return True
    idx_i, idx_j = idx_i_2 - idx_i_1, idx_j_2 - idx_j_1
    if idx_i + 1 > M or idx_j + 1 > M:
        return False
    for rot in range(4):
        for s1 in range(M - idx_i):
            for s2 in range(M - idx_j):
                if match(
                    rot,
                    key,
                    M,
                    lock,
                    N,
                    s1,
                    s2,
                    idx_i,
                    idx_j,
                    idx_i_1,
                    idx_j_1,
                    idx_i_2,
                    idx_j_2,
                ):
                    return True
    return False
