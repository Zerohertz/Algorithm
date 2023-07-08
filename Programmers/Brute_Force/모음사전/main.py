from itertools import product


def solution(word):
    char = ["A", "E", "I", "O", "U"]
    tmp = []
    for i in range(1, 6):
        for j in product(char, repeat=i):
            tmp.append("".join(list(j)))
    tmp.sort()
    return tmp.index(word) + 1
