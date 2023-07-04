import heapq


def solution(scoville, K):
    answer, res = 0, 0
    heapq.heapify(scoville)
    try:
        while True:
            legacy = heapq.heappop(scoville)
            if legacy >= K:
                break
            res = legacy + heapq.heappop(scoville) * 2
            heapq.heappush(scoville, res)
            answer += 1
    except BaseException:
        answer = -1
    return answer
