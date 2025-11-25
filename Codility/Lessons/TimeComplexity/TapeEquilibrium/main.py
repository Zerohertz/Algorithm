def solution(A):
    left, right = A[0], sum(A[1:])
    ans = abs(left - right)
    for i in range(1, len(A) - 1):
        left += A[i]
        right -= A[i]
        ans = min(ans, abs(left - right))
    return ans
