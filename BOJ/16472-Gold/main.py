import sys

read = sys.stdin.readline

N = int(read())
S = read().strip()
idx1 = 0
idx2 = 0
dict = {}
res = [0, 0]

while idx1 < len(S) and idx2 < len(S):
    if S[idx2] not in dict:
        dict[S[idx2]] = 1
    else:
        dict[S[idx2]] += 1
    if len(dict) > N:
        while idx1 <= idx2 and len(dict) > N:
            if dict[S[idx1]] == 1:
                dict.pop(S[idx1])
            else:
                dict[S[idx1]] -= 1
            idx1 += 1
    if len(dict) <= N:
        if res[1] - res[0] < idx2 - idx1:
            res[0] = idx1
            res[1] = idx2
    idx2 += 1

print(res[1] - res[0] + 1)
