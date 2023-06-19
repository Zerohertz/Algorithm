import sys
from itertools import combinations
import heapq
read = sys.stdin.readline


if __name__ == "__main__":
    S = read().strip()
    N = len(S)
    candidates = []
    for i, j in combinations(range(1, N), 2):
        a, b, c = S[:i], S[i:j], S[j:]
        tmp = a[::-1] + b[::-1] + c[::-1]
        heapq.heappush(candidates, tmp)
    print(heapq.heappop(candidates))