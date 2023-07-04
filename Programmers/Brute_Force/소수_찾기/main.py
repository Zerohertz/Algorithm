from itertools import permutations


def cPN(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def solution(numbers):
    answer = []
    tmp = []
    numbers = list(numbers)
    for i in range(1, len(numbers) + 1):
        tmp += permutations(numbers, i)
    num = [int(''.join(t)) for t in tmp]
    for i in num:
        if cPN(i):
            answer.append(i)
    return len(set(answer))
