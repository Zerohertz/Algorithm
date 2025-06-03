import sys

read = sys.stdin.readline

if __name__ == "__main__":
    N = int(read())
    values = [0 for _ in range(N)]
    for i in range(N):
        values[i] = int(read())
    stack = []
    result = 0
    for i in range(N + 1):
        while stack and (i == N or values[stack[-1]] > values[i]):
            height = values[stack[-1]]
            stack.pop()
            width = i
            if stack:
                width = i - stack[-1] - 1
            result = max(result, width * height)
        stack.append(i)
    print(result)

"""
1. Segment Tree
아래와 같이 처음 한번 통과했지만, 그 이후로는 모두 시간 초과.

제출 번호	아이디	문제	결과	메모리	시간	언어	코드 길이	제출한 시간
73379180	zerohertz	 1725	시간 초과			Python 3 / 수정	1702	1년 전
73379145	zerohertz	 1725	시간 초과			Python 3 / 수정	1701	1년 전
73379098	zerohertz	 1725	시간 초과			Python 3 / 수정	1776	1년 전
73379063	zerohertz	 1725	시간 초과			Python 3 / 수정	1783	1년 전
73379022	zerohertz	 1725	시간 초과			Python 3 / 수정	1769	1년 전
73379002	zerohertz	 1725	메모리 초과			Python 3 / 수정	1772	1년 전
73378944	zerohertz	 1725	시간 초과			Python 3 / 수정	1704	1년 전
73378891	zerohertz	 1725	시간 초과			Python 3 / 수정	2471	1년 전
73378879	zerohertz	 1725	런타임 에러 (IndexError)			Python 3 / 수정	2468	1년 전
73378856	zerohertz	 1725	시간 초과			Python 3 / 수정	2307	1년 전
73378764	zerohertz	 1725	맞았습니다!!	62892	3384	Python 3 / 수정	1702	1년 전

import sys

read = sys.stdin.readline
sys.setrecursionlimit(10**6)


def _init(node, start, end):
    if start == end:
        tree[node] = start
        return tree[node]
    mid = (start + end) // 2
    idx1 = _init(node * 2, start, mid)
    idx2 = _init(node * 2 + 1, mid + 1, end)
    if values[idx1] < values[idx2]:
        tree[node] = idx1
    else:
        tree[node] = idx2
    return tree[node]


def _call(left, right, node, start, end):
    if left > end or right < start:
        return -1
    if left <= start and end <= right:
        return tree[node]
    mid = (start + end) // 2
    idx1 = _call(left, right, 2 * node, start, mid)
    idx2 = _call(left, right, 2 * node + 1, mid + 1, end)
    if idx1 == -1:
        return idx2
    elif idx2 == -1:
        return idx1
    if values[idx1] < values[idx2]:
        return idx1
    return idx2


def large(start, end):
    if start == end:
        return values[start]
    idx = _call(start, end, 1, 0, length - 1)
    area = (end - start + 1) * values[idx]
    if start <= idx - 1:
        tmp = large(start, idx - 1)
        area = max(area, tmp)
    if idx + 1 <= end:
        tmp = large(idx + 1, end)
        area = max(area, tmp)
    return area


if __name__ == "__main__":
    N = int(read())
    values = [0 for _ in range(N)]
    for i in range(N):
        values[i] = int(read())
    length = len(values)
    size = 0
    while True:
        if N > 2**size:
            size += 1
        else:
            size += 1
            break
    tree = [0 for _ in range(2**size)]
    _init(1, 0, length - 1)
    print(large(0, length - 1))
"""
