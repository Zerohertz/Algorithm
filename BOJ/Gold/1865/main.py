import sys

read = sys.stdin.readline
INF = int(1e9)


def bf(start):
    distance = [INF for _ in range(N + 1)]
    distance[start] = 0
    for i in range(N):
        for road in roads:
            tmp = road[0]
            next = road[1]
            time = road[2]
            if distance[next] > time + distance[tmp]:
                distance[next] = time + distance[tmp]
                if i == N - 1:
                    return True
    return False


TC = int(read())

for _ in range(TC):
    N, M, W = map(int, read().split())
    roads = []
    for _ in range(M):
        S, E, T = map(int, read().split())
        roads.append((S, E, T))
        roads.append((E, S, T))
    for _ in range(W):
        S, E, T = map(int, read().split())
        roads.append((S, E, -T))
    if bf(1):
        print("YES")
    else:
        print("NO")
