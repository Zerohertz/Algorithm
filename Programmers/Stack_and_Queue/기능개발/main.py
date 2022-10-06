from collections import deque

def solution(progresses, speeds):
    p = deque(progresses)
    s = deque(speeds)
    answer = []
    while p:
        for i in range(len(p)):
            p[i] += s[i]
        tmp = 0
        while p:
            if p[0] >= 100:
                p.popleft()
                s.popleft()
                tmp += 1
            else:
                if tmp > 0:
                    answer.append(tmp)
                break
    answer.append(tmp)
    return answer