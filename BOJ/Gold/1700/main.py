import sys

read = sys.stdin.readline

N, K = map(int, read().split())
l = list(map(int, read().split()))
tap = []
cnt = 0

for i, j in enumerate(l):
    if not j in tap:
        if len(tap) >= N:
            idx = -1
            tmp = l[i:]
            for k in tap:
                if k in tmp:
                    tar = tmp.index(k)
                    if idx < tar:
                        idx = tar
                        val = k
                else:
                    val = k
                    break
            tap[tap.index(val)] = j
            cnt += 1
        else:
            tap.append(j)

print(cnt)
