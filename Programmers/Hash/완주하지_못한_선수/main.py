from collections import Counter

def solution(participant, completion):
    participant.sort()
    completion.sort()
    answer = Counter(participant) - Counter(completion)
    answer = list(answer)[0]
    return answer