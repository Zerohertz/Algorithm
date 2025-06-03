import sys

read = sys.stdin.readline


def bisect():
    result = 0
    left, right = 0, zip[-1] - zip[0]
    while left <= right:
        # 최대 공유기의 거리
        mid = (left + right) // 2
        # 시작 집의 좌표
        tmp = zip[0]
        # 공유기 설치
        cnt = 1
        for i in range(1, N):
            # 현재 좌표와 최대 공유기 거리의 합이
            # (최대 공유기 거리를 유지하는 다음 집의 좌표)
            # 다음 집의 좌표보다 작다면
            if tmp + mid <= zip[i]:
                # 공유기를 설치하고
                cnt += 1
                # 현재 좌표 update
                tmp = zip[i]
        # 설치 공유기의 수를 만족 한다면
        if C <= cnt:
            # 최대 공유기의 거리를 증가
            left = mid + 1
            # 결과 update
            result = mid
        # 설치 공유기의 수를 만족하지 못한다면
        else:
            # 최대 공유기의 거리를 증가
            right = mid - 1
    return result


def main():
    zip.sort()
    print(bisect())


if __name__ == "__main__":
    N, C = map(int, read().split())
    zip = [0 for _ in range(N)]
    for i in range(N):
        zip[i] = int(read())
    main()

"""1st
import sys

read = sys.stdin.readline

if __name__ == "__main__":
    N, C = map(int, read().split())
    coord = [0 for _ in range(N)]
    for i in range(N):
        coord[i] = int(read())
    coord.sort()
    left, right = 1, coord[-1] - coord[0]
    res = 0
    while left <= right:
        mid = (left + right) // 2
        tmp = coord[0]
        cnt = 1
        for i in range(1, N):
            if coord[i] >= tmp + mid:
                cnt += 1
                tmp = coord[i]
        if cnt >= C:
            left = mid + 1
            res = mid
        else:
            right = mid - 1
    print(res)
"""
