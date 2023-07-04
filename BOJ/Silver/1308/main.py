import datetime
import sys

if __name__ == "__main__":
    read = sys.stdin.readline
    y, m, d = map(int, read().split())
    ty, tm, td = map(int, read().split())

    start_day = datetime.date(y, m, d)
    start_after_1000 = datetime.date(y + 1000, m, d)
    end_day = datetime.date(ty, tm, td)

    result_1000 = start_after_1000 - start_day
    result = end_day - start_day
    if result < result_1000:
        print("D-{}".format(result.days))
    else:
        print("gg")
