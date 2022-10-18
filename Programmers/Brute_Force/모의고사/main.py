def solution(answers):
    l = len(answers)
    supo1 = [i % 5 + 1 for i in range(l)]
    su2 = [2, 1, 2, 3, 2, 4, 2, 5]
    supo2 = [su2[i % 8] for i in range(l)]
    su3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    supo3 = [su3[i % 10] for i in range(l)]
    pnt = [0, 0, 0]
    for s1, s2, s3, ans in zip(supo1, supo2, supo3, answers):
        if s1 == ans:
            pnt[0] += 1
        if s2 == ans:
            pnt[1] += 1
        if s3 == ans:
            pnt[2] += 1
    maxpnt = max(pnt)
    answer = []
    for i in range(3):
        if maxpnt == pnt[i]:
            answer.append(i + 1)
    return answer