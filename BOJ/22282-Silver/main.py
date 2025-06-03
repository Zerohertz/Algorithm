import sys

read = sys.stdin.readline


def main():
    citations.sort(reverse=True)
    h_index = 0
    for i, c in enumerate(citations):
        if i < c:
            h_index = i + 1
        else:
            break
    print(h_index)


if __name__ == "__main__":
    n = int(read())
    citations = [0 for _ in range(n)]
    for i in range(n):
        citations[i] = int(read())
    main()
