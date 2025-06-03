import sys

read = sys.stdin.readline


def binary_search(target, data, status):
    start = 0
    end = N - 1
    while start <= end:
        mid = (start + end) // 2
        if data[mid] == target:
            break
        elif data[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    if status:
        if data[mid] >= target:
            mid -= 1
    else:
        if data[mid] <= target:
            mid += 1
    return mid


if __name__ == "__main__":
    N, M = map(int, read().rstrip().split())
    point = list(map(int, read().rstrip().split()))
    point.sort()
    for _ in range(M):
        start, end = map(int, read().rstrip().split())
        start_i = binary_search(start, point, True)
        end_i = binary_search(end, point, False)
        print(end_i - start_i - 1)
