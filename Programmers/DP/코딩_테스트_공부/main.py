def solution(alp, cop, problems):
    taralp = 0
    tarcop = 0
    for a, b, c, d, e in problems:
        taralp = max(taralp, a)
        tarcop = max(tarcop, b)
    alp, cop = min(alp, taralp), min(cop, tarcop)
    dp = [[3000 for _ in range(tarcop + 1)] for _ in range(taralp + 1)]
    dp[alp][cop] = 0
    for i in range(alp, taralp + 1):
        for j in range(cop, tarcop + 1):
            if i + 1 <= taralp:
                dp[i + 1][j] = min(dp[i + 1][j], dp[i][j] + 1)
            if j + 1 <= tarcop:
                dp[i][j + 1] = min(dp[i][j + 1], dp[i][j] + 1)
            for a, b, c, d, e in problems:
                if i >= a and j >= b:
                    nalp, ncop = min(taralp, i + c), min(tarcop, j + d)
                    dp[nalp][ncop] = min(dp[nalp][ncop], dp[i][j] + e)
    return dp[-1][-1]
