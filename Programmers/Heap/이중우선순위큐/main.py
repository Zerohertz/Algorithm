import heapq


def solution(operations):
    mheap = []
    Mheap = []
    for oper in operations:
        tmpoper = oper.split()
        if tmpoper[0] == 'I':
            heapq.heappush(mheap, int(tmpoper[1]))
            heapq.heappush(Mheap, ((-int(tmpoper[1])), int(tmpoper[1])))
        elif tmpoper[0] == 'D':
            if not mheap:
                pass
            elif tmpoper[1] == '1':
                tmp = heapq.heappop(Mheap)
                mheap.remove(tmp[1])
            elif tmpoper[1] == '-1':
                tmp = heapq.heappop(mheap)
                Mheap.remove((-tmp, tmp))
    if mheap:
        answer = [heapq.heappop(Mheap)[1], heapq.heappop(mheap)]
    else:
        answer = [0, 0]
    return answer
