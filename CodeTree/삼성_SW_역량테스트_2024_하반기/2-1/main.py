import sys
from collections import deque

read = sys.stdin.readline

# 상, 하, 좌, 우 우선 순위 방향
DR1 = [-1, 1, 0, 0]
DC1 = [0, 0, -1, 1]

# 좌, 우, 상, 하 우선 순위 방향
DR2 = [0, 0, -1, 1]
DC2 = [-1, 1, 0, 0]


class Medusa:
    def __init__(self, S_r, S_c, E_r, E_c):
        self.r = S_r
        self.c = S_c
        parent = self._get_path(S_r, S_c, E_r, E_c)
        if parent is None:
            print(-1)
            exit()
        self.paths = self._backtrack(S_r, S_c, E_r, E_c, parent)

    def _get_path(self, S_r, S_c, E_r, E_c):
        parent = [[0 for _ in range(N)] for _ in range(N)]
        queue = deque([(S_r, S_c, 0)])
        while queue:
            r, c, cnt = queue.popleft()
            if r == E_r and c == E_c:
                return parent
            for dr, dc in zip(DR1, DC1):
                nr, nc = r + dr, c + dc
                if not (
                    0 <= nr < N
                    and 0 <= nc < N
                    and parent[nr][nc] == 0
                    and fields[nr][nc] == 0
                ):
                    continue
                parent[nr][nc] = (r, c)
                queue.append((nr, nc, cnt + 1))

    def _backtrack(self, S_r, S_c, E_r, E_c, parent):
        paths = []
        while True:
            E_r, E_c = parent[E_r][E_c]
            if (E_r, E_c) == (S_r, S_c):
                break
            paths.append((E_r, E_c))
        return paths[::-1]

    def __getitem__(self, idx):
        self.r, self.c = self.paths[idx]
        return self.paths[idx]

    def move(self, warriors):
        died = []
        for i, warrior in enumerate(warriors):
            if self.r == warrior.r and self.c == warrior.c:
                died.append(i)
        for i in died[::-1]:
            fields[warriors[i].r][warriors[i].c] -= 100
            warriors.pop(i)
        return warriors

    def rotate(self):
        # 상, 하, 좌, 우
        cnt = 0
        stone_field = []
        for i, (dr, dc) in enumerate(zip(DR1, DC1)):
            tmp, _cnt = self.watch(i, dr, dc)
            if cnt < _cnt:
                stone_field = tmp
                cnt = _cnt
        return stone_field, cnt

    def watch(self, direction, dr, dc):
        # direction: 상, 하, 좌, 우 (0, 1, 2, 3)
        cnt = 0
        """
        0: 방문 X
        1: 석화 가능 지역 O
        -1: 석화 가능 지역 X
        """
        stone_field = [[0 for _ in range(N)] for _ in range(N)]
        if direction == 0:
            range_r = range(self.r + dr, -1, -1)
        elif direction == 1:
            range_r = range(self.r + dr, N)
        elif direction == 2:
            range_c = range(self.c + dc, -1, -1)
        elif direction == 3:
            range_c = range(self.c + dc, N)
        if direction < 2:
            for j, r in enumerate(range_r):
                size = j + 1
                c0 = max(self.c - size, 0)
                c1 = min(self.c + size + 1, N)
                for c in range(c0, c1):
                    # 이전 차례에 현재 구역이 석화 불가능 지역으로 정의되지 않으면
                    if stone_field[r][c] == 0:
                        # 현재 구역은 석화 가능 지역
                        stone_field[r][c] = 1
                    # 다음 차례가 있고 현재 구역이 전사가 있거나 석화가 불가능한 곳일 때
                    nr = r + dr
                    if (0 <= nr < N) and (
                        (stone_field[r][c] == 1 and 100 <= fields[r][c])
                        or stone_field[r][c] == -1
                    ):
                        # 하위 구역들도 석화가 불가능 한 곳
                        stone_field[nr][c] = -1
                        if c < self.c and c != 0:
                            stone_field[nr][c - 1] = -1
                        elif self.c < c and c != N - 1:
                            stone_field[nr][c + 1] = -1
                    # 현재 구역이 석화 가능하고 전사가 있을 때
                    if stone_field[r][c] == 1 and 100 <= fields[r][c]:
                        # 석화된 전사 추가
                        cnt += fields[r][c] // 100
        else:
            for j, c in enumerate(range_c):
                size = j + 1
                r0 = max(self.r - size, 0)
                r1 = min(self.r + size + 1, N)
                for r in range(r0, r1):
                    # 이전 차례에 현재 구역이 석화 불가능 지역으로 정의되지 않으면
                    if stone_field[r][c] == 0:
                        # 현재 구역은 석화 가능 지역
                        stone_field[r][c] = 1
                    # 다음 차례가 있고 현재 구역이 전사가 있거나 석화가 불가능한 곳일 때
                    nc = c + dc
                    if (0 <= nc < N) and (
                        (stone_field[r][c] == 1 and 100 <= fields[r][c])
                        or stone_field[r][c] == -1
                    ):
                        # 하위 구역들도 석화가 불가능 한 곳
                        stone_field[r][nc] = -1
                        if r < self.r and r != 0:
                            stone_field[r - 1][nc] = -1
                        elif self.r < r and r != N - 1:
                            stone_field[r + 1][nc] = -1
                    # 현재 구역이 석화 가능하고 전사가 있을 때
                    if stone_field[r][c] == 1 and 100 <= fields[r][c]:
                        # 석화된 전사 추가
                        cnt += fields[r][c] // 100
        return stone_field, cnt


class Warrior:
    def __init__(self, r, c):
        self.r = r
        self.c = c
        # fields 100 당 전사 1명
        fields[r][c] += 100

    def move(self, medusa, stone_field):
        """
        Returns:
            전사가 움직인 횟수
            삭제 여부
        """
        M_r, M_c = medusa.r, medusa.c
        cnt = 0
        if stone_field[self.r][self.c] == 1:
            return 0, 0
        for i in range(2):
            dist = self._distance(self.r, self.c, M_r, M_c)
            tr, tc = self.r, self.c
            if i == 0:
                DR, DC = DR1, DC1
            else:
                DR, DC = DR2, DC2
            for dr, dc in zip(DR, DC):
                nr, nc = self.r + dr, self.c + dc
                if not (0 <= nr < N and 0 <= nc < N):
                    continue
                # 석화 구역이면 생략
                if stone_field[nr][nc] == 1:
                    continue
                _dist = self._distance(nr, nc, M_r, M_c)
                if _dist < dist:
                    tr, tc = nr, nc
                    dist = _dist
            # 움직일 수 없는 상태라면 정지
            if self.r == tr and self.c == tc:
                return cnt, 0
            # 최종 이동 좌표
            fields[self.r][self.c] -= 100
            fields[tr][tc] += 100
            self.r, self.c = tr, tc
            cnt += 1
            if self.r == M_r and self.c == M_c:
                fields[self.r][self.c] -= 100
                return cnt, 1
        return cnt, 0

    def _distance(self, r, c, M_r, M_c):
        return abs(M_r - r) + abs(M_c - c)


def simulation(medusa, warriors):
    """
    1. 메두사의 이동
        1-1. 메두사는 도로를 따라 한 칸 이동 (집 -> 공원 최단 경로)
        1-2. 메두사의 이동 칸에 전사 발견 시 전사는 삭제
    2. 메두사의 시선
        2-1. 상, 하, 좌, 우 하나의 방향 선택 (가장 많은 전사가 돌로 변화하는 기준, 상하좌우 우선순위)
        2-2. 8방향 기준으로 전사 뒤의 전사에는 영향을 주지 못함
        2-3. 메두사가 본 전사들은 모두 돌로 변하여 현재 턴 이동 불가
        2-4. 두 명 이상의 전사가 동일 칸 위치 시 모두 돌로 변화
    3. 전사들의 이동
        3-1. 메두사와의 거리를 줄일 수 있는 방향으로 한 칸 이동 (상하좌우 우선순위, 격자 밖 및 메두사 시야 안 이동 불가)
        3-2. 메두사와의 거리를 줄일 수 있는 방향으로 한 칸 더 이동 (좌우상하 우선순위, 격자 밖 및 메두사 시야 안 이동 불가)
    4. 전사의 공격
        4-1. 메두사와 같은 칸 도달한 전사는 메두사를 공격 후 사라짐

    Returns:
        1. 모든 전사가 이동한 거리의 합
        2. 메두사로 인해 돌이 된 전사의 수
        3. 메두사를 공격한 전사의 수
        메두사 공원 도착 시 0 출력
    """
    warriors_move_cnt = warriors_attack_cnt = 0
    warriors = medusa.move(warriors)
    stone_field, warriors_stoned_cnt = medusa.rotate()
    died = []
    for i, warrior in enumerate(warriors):
        _warriors_move_cnt, _warriors_attack_cnt = warrior.move(medusa, stone_field)
        warriors_move_cnt += _warriors_move_cnt
        warriors_attack_cnt += _warriors_attack_cnt
        if _warriors_attack_cnt == 1:
            died.append(i)
    for i in died[::-1]:
        warriors.pop(i)
    print(warriors_move_cnt, warriors_stoned_cnt, warriors_attack_cnt)
    return warriors


def main():
    # 메두사 instance
    medusa = Medusa(S_r, S_c, E_r, E_c)

    # 전사 instance
    warriors = []
    for i in range(len(A) // 2):
        W_r, W_c = A[2 * i], A[2 * i + 1]
        warrior = Warrior(W_r, W_c)
        warriors.append(warrior)

    for mr, mc in medusa:
        warriors = simulation(medusa, warriors)
    print(0)


if __name__ == "__main__":
    # N: 마을의 크기
    # M: 전사들의 수
    N, M = map(int, read().split())

    # S: 메두사의 집 좌표
    # E: 공원의 좌표
    S_r, S_c, E_r, E_c = map(int, read().split())

    # A: 전사들의 좌표
    A = list(map(int, read().split()))

    # fields: 도로 정보
    # 0: 도로 O / 1: 도로 X
    # 메두사는 0인 곳만 이동 가능
    fields = []
    for _ in range(N):
        fields.append(list(map(int, read().split())))

    main()


"""
In[0]

6 4
3 1 1 2
3 5 1 4 0 4 1 3
0 0 0 0 1 0
0 1 0 0 1 1
1 1 0 0 0 0
0 0 1 0 1 1
0 0 0 0 0 0
0 0 0 0 1 1

Ans[0]

3 2 0
2 2 1
0 2 0
0 2 0
0 2 0
1 1 1
0

Out[0]

4 2 0 -> 한 칸 덜 가야하는데 더 갔음 -> 석화 문제? -> 석화 2인에 대해는 맞기 때문에 warrior.move에 문제있는 것으로 파악
4 2 1
2 2 0
2 2 0
2 2 0
1 1 1
0

X: 메두사
V: 전사
S: 석화

0 0 0 0 V 0
0 1 0 V V 1
1 1 0 0 0 0
0 X 1 0 1 V
0 0 0 0 0 0
0 0 0 0 1 1

S S S 0 V 0
S S S V V 1
S S S S 0 0
S S S 0 1 V
0 X 0 0 0 0
0 0 0 0 1 1

메두사가 위를 볼 때 2명만 석화 -> 최상단의 전사는 한 번만 움직일 수 있음
(0, 4) -> (0, 3)
"""

"""
In[1]

6 4
3 1 1 2
3 5 1 4 0 4 1 3
0 0 0 0 1 0
0 1 0 0 1 1
1 1 0 0 0 0
0 0 1 0 1 1
0 0 0 0 0 0
0 0 0 0 1 1

Ans[1]

3 2 0
2 2 1
0 2 0
0 2 0
0 2 0
1 1 1
0

Out[1]

3 2 0
4 2 1 -> 전사가 또 2번 더 이동함 -> 움직일 수 없는 상태임에도 불구하고 올바르게 정지되지 않음
2 2 0
2 2 0
2 2 0
1 1 1
0

S S S V 0 0
S S S V V S
S S S S S 0
0 S S S 1 0
0 0 X 0 V 0
0 0 0 0 1 1
"""

"""
In[2]

7 4
1 1 5 0
5 3 4 5 6 3 3 1
0 0 0 0 0 1 0
0 0 0 1 0 1 0
0 1 1 0 0 0 0
1 0 0 0 0 0 0
0 0 1 0 0 0 0
0 0 0 0 0 1 0
0 0 0 0 1 0 0

Ans[2]

0 3 0
0 3 0
0 3 0
0 3 0
2 2 0
2 2 1
0 2 0
1 1 1
0 2 0
0 1 0
0 1 0
0 1 0
0

Out[2]

0 3 0
0 3 0
0 3 0
0 3 0
2 2 0
2 2 0 -> 전사 하나가 공격하지 못했음
2 2 0
3 2 1
1 1 1
0 1 0
0 1 0
0 1 0
0

처음은 상하좌우, 다음은 좌우상하로 움직임
"""
