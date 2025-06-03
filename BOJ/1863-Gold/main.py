"""
제출 번호	아이디	문제	결과	메모리	시간	언어	코드 길이	제출한 시간
73368993	zerohertz	 1863	맞았습니다!!	31120	52	Python 3 / 수정	424	19초 전
"""

import sys

read = sys.stdin.readline

if __name__ == "__main__":
    n = int(read())
    cnt = 0
    height = [0]
    for i in range(n + 2):
        if i in [0, n + 1]:
            x, y = 0, 0
        else:
            x, y = map(int, read().split())
        while 1 < len(height) and y < height[-1]:
            height.pop()
            cnt += 1
        if not height[-1] == y:
            height.append(y)
    print(cnt)

"""
4
1 3
2 2
3 4
4 2

3
"""

"""
3
1 4
2 2
3 4

3
"""

"""
4
1 2
2 4
3 2
4 3

3
"""

"""
4
1 2
2 4
3 3
4 0

3
"""
