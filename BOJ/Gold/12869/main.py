from itertools import permutations

def solution(x, y, z, cnt):
    global ans
    if x <= 0 and y <= 0 and z <= 0:
        if ans > cnt:
            ans = cnt
            return
    x = 0 if x <= 0 else x
    y = 0 if y <= 0 else y
    z = 0 if z <= 0 else z
    if dp[x][y][z] <= cnt and dp[x][y][z] != 0:
        return
    dp[x][y][z] = cnt
    for i, j, k in permutations([9, 3, 1], 3):
        solution(x - i, y - j, z - k, cnt + 1)

N = int(input())
SCV = list(map(int, input().split()))
while len(SCV) < 3:
    SCV += [0]
ans = 100
dp = [[[100] * (max(SCV) + 1) for i in range((max(SCV) + 1))] for j in range((max(SCV) + 1))]
solution(SCV[0], SCV[1], SCV[2], 0)
print(ans)