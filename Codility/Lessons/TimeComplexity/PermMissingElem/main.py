def solution(A):
    N = len(A)
    if N == 0:
        return 1
    A.sort()
    for i, j in enumerate(A):
        if i + 1 == j:
            continue
        return i + 1
    return N + 1
