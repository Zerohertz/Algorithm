import sys
from collections import deque

read = sys.stdin.readline

N, M = map(int, read().split())

l = [[0 for _ in range(M)] for _ in range(N)]
pos = {"R": [], "B": []}
for i in range(N):
    l[i] = list(read().rstrip())
    for j in range(M):
        if l[i][j] == "R":
            pos["R"] = [i, j]
            l[i][j] = "."
        elif l[i][j] == "B":
            pos["B"] = [i, j]
            l[i][j] = "."

dirdict = {0: (1, 0), 1: (0, 1), 2: (-1, 0), 3: (0, -1)}


def gravity(tmppos, direction):
    status = 0
    rx, ry = tmppos["R"]
    bx, by = tmppos["B"]
    v1, v2 = dirdict[direction]
    RedGoalIn = False
    while True:
        if l[rx + v1][ry + v2] != "#" or l[bx +
                                           v1][by + v2] != "#":  # 둘 중 하나가 이동 가능할 때
            if l[rx + v1][ry + v2] != "#" and not RedGoalIn:  # Red 이동
                rx += v1
                ry += v2
                majimak = True
            if l[bx + v1][by + v2] != "#":  # Blue 이동
                bx += v1
                by += v2
                majimak = False
        if l[rx][ry] == "O":
            RedGoalIn = True
        if l[bx][by] == "O":
            status = -100
            return tmppos, status
        if (
            l[rx + v1][ry + v2] == "#" and l[bx + v1][by + v2] == "#"
        ):  # 둘 다 이동 불가 시 이동 정지
            break
        if (
            RedGoalIn and l[bx + v1][by + v2] == "#"
        ):  # Red가 구멍으로 들어가고 Blue는 이동 불가 시 이동 정지
            break
    if rx == bx and ry == by:  # Red와 Blue 충돌 시
        if majimak:
            rx -= v1
            ry -= v2
        else:
            bx -= v1
            by -= v2
    if RedGoalIn:
        status = 100
    tmppos["R"] = [rx, ry]
    tmppos["B"] = [bx, by]
    return tmppos, status


visit = [
    [[[False for _ in range(M)] for _ in range(N)] for _ in range(M)] for _ in range(N)
]

q = deque([[pos["R"], pos["B"], 0]])
visit[pos["R"][0]][pos["R"][1]][pos["B"][0]][pos["B"][1]] = True

while q:
    RedPos, BluePos, cnt = q.popleft()
    for i in range(4):
        pos["R"] = RedPos
        pos["B"] = BluePos
        a, b = gravity(pos, i)
        if b == 100:
            if cnt + 1 > 10:
                print(-1)
                exit()
            else:
                print(cnt + 1)
                exit()
        else:
            if not visit[a["R"][0]][a["R"][1]][a["B"][0]][a["B"][1]]:
                visit[a["R"][0]][a["R"][1]][a["B"][0]][a["B"][1]] = True
                q.append([a["R"], a["B"], cnt + 1])
print(-1)
