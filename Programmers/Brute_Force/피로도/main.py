from itertools import permutations

def solution(k, dungeons):
    answer = []
    dungeonslist = permutations(dungeons)
    for i in dungeonslist:
        ans = 0
        tmp = k
        for j in i:
            if tmp >= j[0]:
                tmp -= j[1]
                ans += 1
            else:
                continue
        answer.append(ans)
    return max(answer)