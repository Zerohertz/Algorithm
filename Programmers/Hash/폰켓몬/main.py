def solution(nums):
    answer = min(len(nums) // 2, len(set(nums)))
    return answer