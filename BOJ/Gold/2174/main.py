import sys

read = sys.stdin.readline


def turnLeft(robotNo, cnt):
    x, y = pos[robotNo]
    for _ in range(cnt):
        if G[x][y][1:] == [1, 0]:
            G[x][y][1:] = [0, 1]
        elif G[x][y][1:] == [0, 1]:
            G[x][y][1:] = [-1, 0]
        elif G[x][y][1:] == [-1, 0]:
            G[x][y][1:] = [0, -1]
        elif G[x][y][1:] == [0, -1]:
            G[x][y][1:] = [1, 0]


def turnRight(robotNo, cnt):
    x, y = pos[robotNo]
    for _ in range(cnt):
        if G[x][y][1:] == [1, 0]:
            G[x][y][1:] = [0, -1]
        elif G[x][y][1:] == [0, -1]:
            G[x][y][1:] = [-1, 0]
        elif G[x][y][1:] == [-1, 0]:
            G[x][y][1:] = [0, 1]
        elif G[x][y][1:] == [0, 1]:
            G[x][y][1:] = [1, 0]


def goForward(robotNo, cnt):
    status = True
    x, y = pos[robotNo]
    ang = G[x][y][1:]
    for i in range(1, cnt + 1):
        nx = x + ang[0] * i
        ny = y + ang[1] * i
        if not (0 <= nx < A) or not (0 <= ny < B):
            print('Robot ' + str(robotNo + 1) + ' crashes into the wall')
            status = False
            break
        if G[nx][ny][0] != 0:
            print('Robot ' + str(robotNo + 1) +
                  ' crashes into robot ' + str(G[nx][ny][0]))
            status = False
            break
    if status:
        G[nx][ny] = G[x][y]
        G[x][y] = [0, 0, 0]
        pos[robotNo] = [nx, ny]
    return status


A, B = map(int, read().split())
M, N = map(int, read().split())

G = [[[0, 0, 0] for _ in range(B)] for _ in range(A)]
pos = []
ang = {'E': [1, 0], 'N': [0, 1], 'W': [-1, 0], 'S': [0, -1]}

for i in range(M):
    a, b, c = map(str, read().split())
    a, b = int(a) - 1, int(b) - 1
    G[a][b] = [i + 1] + ang[c]
    pos.append([a, b])

commands = []

for _ in range(N):
    commands.append(list(map(str, read().split())))

status = True
for command in commands:
    if command[1] == 'L':
        robotNo = int(command[0]) - 1
        cnt = int(command[2])
        turnLeft(robotNo, cnt)
    elif command[1] == 'R':
        robotNo = int(command[0]) - 1
        cnt = int(command[2])
        turnRight(robotNo, cnt)
    elif command[1] == 'F':
        robotNo = int(command[0]) - 1
        cnt = int(command[2])
        status = goForward(robotNo, cnt)
    if not status:
        break
if status:
    print('OK')
