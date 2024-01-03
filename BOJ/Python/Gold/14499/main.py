import sys

read = sys.stdin.readline


def _move_y_p(dice):
    return {
        "top": dice["left"],
        "right": dice["top"],
        "bottom": dice["right"],
        "left": dice["bottom"],
        "front": dice["front"],
        "rear": dice["rear"],
    }


def _move_y_n(dice):
    return {
        "top": dice["right"],
        "right": dice["bottom"],
        "bottom": dice["left"],
        "left": dice["top"],
        "front": dice["front"],
        "rear": dice["rear"],
    }


def _move_x_p(dice):
    return {
        "top": dice["rear"],
        "bottom": dice["front"],
        "front": dice["top"],
        "rear": dice["bottom"],
        "right": dice["right"],
        "left": dice["left"],
    }


def _move_x_n(dice):
    return {
        "top": dice["front"],
        "bottom": dice["rear"],
        "front": dice["bottom"],
        "rear": dice["top"],
        "right": dice["right"],
        "left": dice["left"],
    }


def move(dice, dir):
    if dir == 1:
        return _move_y_p(dice)
    if dir == 2:
        return _move_y_n(dice)
    if dir == 3:
        return _move_x_n(dice)
    if dir == 4:
        return _move_x_p(dice)


def copy(graph, dice, nx, ny):
    if graph[nx][ny] == 0:
        graph[nx][ny] = dice["bottom"]
    else:
        dice["bottom"] = graph[nx][ny]
        graph[nx][ny] = 0
    print(dice["top"])


DIR = [None, (0, 1), (0, -1), (-1, 0), (1, 0)]

if __name__ == "__main__":
    dice = {
        "top": 0,
        "right": 0,
        "bottom": 0,
        "left": 0,
        "front": 0,
        "rear": 0,
    }
    N, M, x, y, K = map(int, read().split())
    graph = [[0 for _ in range(M)] for _ in range(N)]
    for i in range(N):
        m = list(map(int, read().split()))
        for j, val in enumerate(m):
            graph[i][j] = val
    commands = list(map(int, read().split()))
    for command in commands:
        dx, dy = DIR[command]
        x += dx
        y += dy
        if 0 <= x < N and 0 <= y < M:
            dice = move(dice, command)
            copy(graph, dice, x, y)
        else:
            x -= dx
            y -= dy
