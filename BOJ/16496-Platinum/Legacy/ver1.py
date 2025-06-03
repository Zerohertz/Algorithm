import sys

read = sys.stdin.readline


def masking(num):
    l = len(num)
    return num + (9 - l) * num[0], l


if __name__ == "__main__":
    N = int(read())
    nums = list(map(masking, read().split()))
    nums = sorted(nums, key=lambda n: (int(n[0]), n[1]), reverse=True)
    ans = ""
    for value, length in nums:
        ans += value[:length]
    print(int(ans))

"""
3
98 9 981

998981
"""

"""
2
32 3

332
"""

"""
2
34 3

343
"""

"""
3
123 12 3

312312
"""

"""
2
21 2122

212221
"""

"""
2
12 1211

121211
"""
