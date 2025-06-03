"""
Brute force로 발생 가능한 모든 case: O(3^6C2) = O(14,348,907)
"""

import sys
from itertools import combinations

read = sys.stdin.readline


def mapping(idx, status):
    return 3 * idx + status


def dfs(results, depth=0):
    global res
    if depth == 15:
        if max(results) == 0:
            res = 1
        return
    idx_1, idx_2 = maps[depth]
    for status_1, status_2 in [(0, 2), (1, 1), (2, 0)]:
        idx_1_, idx_2_ = mapping(idx_1, status_1), mapping(idx_2, status_2)
        if results[idx_1_] > 0 and results[idx_2_] > 0:
            results[idx_1_] -= 1
            results[idx_2_] -= 1
            dfs(results, depth + 1)
            results[idx_1_] += 1
            results[idx_2_] += 1


if __name__ == "__main__":
    for _ in range(4):
        maps = list(combinations(range(6), 2))
        res = 0
        dfs(list(map(int, read().split())))
        print(res, end=" ")
