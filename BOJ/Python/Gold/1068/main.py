import sys

read = sys.stdin.readline


def DFS(root):
    Map[root] = -sys.maxsize
    for i in range(N):
        if root == Map[i]:
            DFS(i)


if __name__ == "__main__":
    N = int(read())
    Map = list(map(int, read().split()))
    d = int(read())
    cnt = 0
    DFS(d)
    for i in range(N):
        if not i == -sys.maxsize and not i in Map:
            cnt += 1
    print(cnt)
