import sys

read = sys.stdin.readline


N = int(read())
A = list(map(int, read().split()))
res = [-sys.maxsize]
dp = []

for i in A:
    if res[-1] < i:
        res.append(i)
        dp.append(len(res) - 1)
    else:
        left = 0
        right = len(res)
        while left < right:
            mid = (left + right) // 2
            if res[mid] < i:
                left = mid + 1
            else:
                right = mid
        res[left] = i
        dp.append(left)

print(len(res) - 1)

subseq = []
M = max(dp)
for i in range(N - 1, -1, -1):
    if dp[i] == M:
        subseq.append(A[i])
        M -= 1

print(*subseq[::-1])
