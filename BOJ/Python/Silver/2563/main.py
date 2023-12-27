import sys

read = sys.stdin.readline

if __name__ == "__main__":
    N = int(read())
    dhj = [[False for _ in range(101)] for _ in range(101)]
    for _ in range(N):
        a, b = map(int, read().split())
        for i in range(a, a + 10):
            for j in range(b, b + 10):
                dhj[i][j] = True
    cnt = 0
    for i in range(101):
        for j in range(101):
            if dhj[i][j]:
                cnt += 1
    print(cnt)
