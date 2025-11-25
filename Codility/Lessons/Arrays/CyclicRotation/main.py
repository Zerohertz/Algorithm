def solution(A, K):
    N = len(A)
    K %= N
    K = N - K
    return A[K:] + A[:K]
