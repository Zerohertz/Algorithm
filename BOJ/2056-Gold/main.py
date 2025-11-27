import sys
from collections import deque

read = sys.stdin.readline


def main(jobs: list[list[int]]) -> int:
    times = [0 for _ in range(N)]
    graph = [[] for _ in range(N)]
    deps = [0 for _ in range(N)]
    dp = [0 for _ in range(N)]
    queue = deque()
    for idx, job in enumerate(jobs):
        times[idx] = job[0]
        deps[idx] = job[1]
        for i in range(job[1]):
            graph[job[i + 2] - 1].append(idx)
        if job[1] == 0:
            queue.append(idx)
            dp[idx] = job[0]
    while queue:
        job = queue.popleft()
        for next_job in graph[job]:
            deps[next_job] -= 1
            dp[next_job] = max(dp[next_job], dp[job])
            if deps[next_job] == 0:
                queue.append(next_job)
                dp[next_job] += times[next_job]
    return max(dp)


if __name__ == "__main__":
    N = int(read().strip())
    jobs = []
    for _ in range(N):
        jobs.append(list(map(int, read().strip().split())))
    print(main(jobs))

"""
5
5 0
1 1 1
8 0
4 1 3
3 2 2 4
>>> 15

5
8 0
4 1 1
5 0
1 1 3
3 2 2 4
>>> 15
"""
