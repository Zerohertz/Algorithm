import sys

read = sys.stdin.readline

if __name__ == "__main__":
    N, L = map(int, read().split())
    Map = [[] for _ in range(N)]
    for i in range(N):
        Map[i] = list(map(int, read().split()))
    res = 0
    for i in range(N):
        tmp1 = -1
        down, up = 0, 0
        flag = True
        for j in range(N):
            tmp2 = Map[i][j]
            if down == 0:
                if tmp1 == -1:
                    tmp1 = tmp2
                    up += 1
                elif tmp1 == tmp2:
                    up += 1
                elif tmp1 - tmp2 == 1:
                    tmp1 = tmp2
                    down = L - 1
                    up = 0
                elif tmp1 - tmp2 == -1:
                    if up >= L:
                        tmp1 = tmp2
                        up = 1
                    else:
                        flag = False
                        break
                else:
                    flag = False
                    break
            else:
                if tmp1 == tmp2:
                    down -= 1
                    up = 0
                else:
                    flag = False
                    break
        if down == 0 and flag:
            res += 1
    for i in range(N):
        tmp1 = -1
        down, up = 0, 0
        flag = True
        for j in range(N):
            tmp2 = Map[j][i]
            if down == 0:
                if tmp1 == -1:
                    tmp1 = tmp2
                    up += 1
                elif tmp1 == tmp2:
                    up += 1
                elif tmp1 - tmp2 == 1:
                    tmp1 = tmp2
                    down = L - 1
                    up = 0
                elif tmp1 - tmp2 == -1:
                    if up >= L:
                        tmp1 = tmp2
                        up = 1
                    else:
                        flag = False
                        break
                else:
                    flag = False
                    break
            else:
                if tmp1 == tmp2:
                    down -= 1
                    up = 0
                else:
                    flag = False
                    break
        if down == 0 and flag:
            res += 1
    print(res)
