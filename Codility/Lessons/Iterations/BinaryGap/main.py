def solution(N):
    zeros = bin(N)[2:].split("1")
    if len(zeros) < 3:
        return 0
    ans = 0
    for i in range(1, len(zeros) - 1):
        ans = max(ans, len(zeros[i]))
    return ans
