from collections import deque

def solution(priorities, location):
    priorities = [[i, j] for i, j in enumerate(priorities)]
    priorities = deque(priorities)
    q = deque()
    while priorities:
        M = 0
        for i in priorities:
            M = max(M, i[1])
        tmp = priorities.popleft()
        if tmp[1] != M:
            priorities.append(tmp)
        else:
            q.append(tmp)
            if tmp[0] == location:
                break
    return len(q)