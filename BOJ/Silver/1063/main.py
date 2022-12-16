king, stone, n = input().split()
n = int(n)
king = [ord(king[0]) - ord("A") + 1, int(king[1])]
stone = [ord(stone[0]) - ord("A") + 1, int(stone[1])]

move_types = ["R", "L", "B", "T", "RT", "LT", "RB", "LB"]
dx = [1, -1, 0, 0, 1, -1, 1, -1]
dy = [0, 0, -1, 1, 1, 1, -1, -1]

for _ in range(n):
    move = input()
    idx = move_types.index(move)
    king_delta = [king[0] + dx[idx], king[1] + dy[idx]]
    stone_delta = [stone[0] + dx[idx], stone[1] + dy[idx]]
    if 1 <= king_delta[0] <= 8 and 1 <= king_delta[1] <= 8:
        if king_delta == stone:
            if 1 <= stone_delta[0] <= 8 and 1 <= stone_delta[1] <= 8:
                king = king_delta
                stone = stone_delta
        else:
            king = king_delta

print(chr(king[0] + ord("A") - 1) + str(king[1]))
print(chr(stone[0] + ord("A") - 1) + str(stone[1]))