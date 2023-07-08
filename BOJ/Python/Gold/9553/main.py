import math


def probability(x1, y1, x2, y2):
    return (
        math.acos(
            (x1 * x2 + y1 * y2) / math.sqrt((x1**2 + y1**2) * (x2**2 + y2**2))
        )
    ) / (2 * math.pi)


for tc in range(int(input())):
    print(
        format(
            sum(
                [
                    probability(*list(map(int, input().split())))
                    for i in range(int(input()))
                ]
            ),
            ".5f",
        )
    )
