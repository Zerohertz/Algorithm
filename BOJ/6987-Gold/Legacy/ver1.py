"""
Brute force로 발생 가능한 모든 case: O(3^6C2) = O(14,348,907)
"""

import sys
from itertools import combinations, permutations

read = sys.stdin.readline


def preprocess(results):
    for i in range(6):
        if 5 != sum(results[i * 3 : (i + 1) * 3]):
            return False
    win, draw, lose = sum(results[0:18:3]), sum(results[1:18:3]), sum(results[2:18:3])
    if (win != lose) or (draw % 2 == 1) or (win + draw / 2 != 15):
        return False
    return True


def _validation(results, idx1, idx2):
    if results[idx1] > 0 and results[idx2] > 0:
        results[idx1] -= 1
        results[idx2] -= 1
        return True
    return False


def validation(results):
    if not preprocess(results):
        return 0
    visited = {}
    for i, j in combinations(range(6), 2):
        visited[f"{i}-{j}"] = False
    for i, j in permutations(range(6), 2):
        if visited[f"{min(i, j)}-{max(i, j)}"]:
            continue
        win, lose = i * 3, j * 3 + 2
        draw_1, draw_2 = i * 3 + 1, j * 3 + 1
        if _validation(results, win, lose):
            visited[f"{min(i, j)}-{max(i, j)}"] = True
            continue
        visited[f"{min(i, j)}-{max(i, j)}"] = _validation(results, draw_1, draw_2)
    return 1 if (max(results) == 0 and min(visited.values())) else 0


if __name__ == "__main__":
    for _ in range(4):
        print(validation(list(map(int, read().split()))), end=" ")
