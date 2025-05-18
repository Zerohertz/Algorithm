def init(node, start, end):
    if start == end:
        tree[node] = l[start]
        return tree[node]
    else:
        tree[node] = init(node * 2, start, (start + end) // 2) + init(
            node * 2 + 1, (start + end) // 2 + 1, end
        )
        return tree[node]


def segUpdate(node, start, end, idx, diff):
    if idx < start or idx > end:
        return
    tree[node] += diff
    if start != end:
        segUpdate(node * 2, start, (start + end) // 2, idx, diff)
        segUpdate(node * 2 + 1, (start + end) // 2 + 1, end, idx, diff)


def segSum(node, start, end, left, right):
    if left > end or right < start:
        return 0
    if left <= start and end <= right:
        return tree[node]
    return segSum(node * 2, start, (start + end) // 2, left, right) + segSum(
        node * 2 + 1, (start + end) // 2 + 1, end, left, right
    )
