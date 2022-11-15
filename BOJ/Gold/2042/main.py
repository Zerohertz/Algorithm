import sys
read = sys.stdin.readline

def init(node, start, end):
  if start == end:
    tree[node] = l[start]
    return tree[node]
  else:
    tree[node] = init(node * 2, start, (start + end) // 2) + init(node * 2 + 1, (start + end) // 2 + 1, end)
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
  return segSum(node * 2, start, (start + end) // 2, left, right) + segSum(node * 2 + 1, (start + end) // 2 + 1, end, left, right)

N, M, K = map(int, read().split())

l = [0 for _ in range(N)]
for i in range(N):
  l[i] = int(read())

tree = [0 for _ in range(4_000_000)]
init(1, 0, N - 1)

for _ in range(M + K):
  a, b, c = map(int, read().split())
  if a == 1:
    b -= 1
    diff = c - l[b]
    l[b] = c
    segUpdate(1, 0, N - 1, b, diff)
  elif a == 2:
    print(segSum(1, 0, N - 1, b - 1, c - 1))