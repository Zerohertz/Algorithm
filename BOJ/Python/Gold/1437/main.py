import sys

read = sys.stdin.readline

if __name__ == "__main__":
    N = int(read().strip())
    if N < 5:
        print(N)
    elif N % 3 == 0:
        print(pow(3, N // 3, 10_007))
    elif N % 3 == 1:
        print((pow(3, (N - 4) // 3, 10_007) * 4) % 10_007)
    else:
        print((pow(3, (N - 2) // 3, 10_007) * 2) % 10_007)
