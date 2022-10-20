from collections import deque
from itertools import combinations

def BFS(n, wiresmap):
    q = deque([])
    visit = [False for _ in range(n + 1)]
    cnt0, cnt1 = 0, 0
    status = True
    for i in range(1, n + 1):
        if not visit[i]:
            q.append(i)
            while q:
                tmp = q.popleft()
                if status:
                    cnt0 += 1
                else:
                    cnt1 += 1
                visit[tmp] = True
                for j in wiresmap[tmp]:
                    if not visit[j]:
                        q.append(j)
            status = False
    return abs(cnt0 - cnt1)

def solution(n, wires):
    answer = []
    for wire in combinations(wires, len(wires) - 1):
        wiresmap = [[] for _ in range(n + 1)]
        for i in wire:
            wiresmap[i[0]].append(i[1])
            wiresmap[i[1]].append(i[0])
        answer.append(BFS(n, wiresmap))
    return min(answer)