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
