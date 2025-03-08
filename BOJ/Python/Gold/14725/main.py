import sys

read = sys.stdin.readline


class Trie:
    def __init__(self) -> None:
        self.root = {}

    def add(self, values: list[str]) -> None:
        tmp = self.root
        for value in values:
            if value not in tmp:
                tmp[value] = {}
            tmp = tmp[value]
        tmp[0] = True

    def dfs(self, tmp: None | dict = None, depth: int = 0) -> None:
        if tmp is None:
            tmp = self.root
        if 0 in tmp:
            return
        for value in tmp:
            print("--" * depth + value)
            self.dfs(tmp[value], depth + 1)


def main():
    N = int(read())
    caves = []
    for i in range(N):
        caves.append(read().strip()[2:])
    caves.sort()
    trie = Trie()
    for cave in caves:
        trie.add(list(cave.split()))
    trie.dfs()


if __name__ == "__main__":
    main()
