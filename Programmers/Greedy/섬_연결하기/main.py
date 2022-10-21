def solution(n, costs):
    answer = 0
    costs.sort(key = lambda x: x[2])
    s = set([costs[0][0]])
    while len(s) != n:
        for i, cost in enumerate(costs):
            if cost[0] in s and cost[1] in s:
                continue
            if cost[0] in s or cost[1] in s:
                s.update([cost[0], cost[1]])
                answer += cost[2]
                break
    return answer