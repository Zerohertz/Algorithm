#!/bin/python3


#
# Complete the 'findMinimumPlansForBandwidth' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY planSizes
#  2. INTEGER targetBandwidth
#


def findMinimumPlansForBandwidth(planSizes, targetBandwidth):
    if targetBandwidth == 0:
        return 0
    MAX = targetBandwidth + 1
    dp = [MAX for _ in range(MAX + 1)]
    dp[0] = 0
    for plan in planSizes:
        for i in range(plan, MAX + 1):
            if dp[i - plan] == MAX:
                continue
            if dp[i - plan] + 1 < dp[i]:
                dp[i] = dp[i - plan] + 1
    return -1 if dp[targetBandwidth] == MAX else dp[targetBandwidth]
    """
    NOTE: DP
    if targetBandwidth == 0:
        return 0
    planSizes.sort()
    queue = deque([(0, 0)])
    while queue:
        bandwith, cnt = queue.pop()
        for plan in planSizes:
            _bandwith = bandwith + plan
            if targetBandwidth < _bandwith:
                continue
            if _bandwith == targetBandwidth:
                return cnt + 1
            queue.append((_bandwith, cnt + 1))
    return -1
    """


if __name__ == "__main__":
    planSizes_count = int(input().strip())

    planSizes = []

    for _ in range(planSizes_count):
        planSizes_item = int(input().strip())
        planSizes.append(planSizes_item)

    targetBandwidth = int(input().strip())

    result = findMinimumPlansForBandwidth(planSizes, targetBandwidth)

    print(result)
