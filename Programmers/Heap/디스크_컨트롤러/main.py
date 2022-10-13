import heapq

def solution(jobs):
    answer = 0
    end, i = 0, 0
    start = -1
    h = []
    while len(jobs) > i:
        for job in jobs:
            if start < job[0] <= end:
                heapq.heappush(h, (job[1], job[0]))
        if len(h) > 0:
            tmp = heapq.heappop(h)
            start = end
            end += tmp[0]
            answer += (end - tmp[1])
            i += 1
        else:
            end += 1
    answer = answer // len(jobs)
    return answer