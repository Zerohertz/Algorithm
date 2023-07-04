import heapq


def solution(genres, plays):
    answer = []
    d = {}
    ds = {}
    idx = 0
    for genre, play in zip(genres, plays):
        try:
            heapq.heappush(d[genre], (-play, idx))
            ds[genre] += play
        except BaseException:
            d[genre] = [(-play, idx)]
            ds[genre] = play
        idx += 1
    l = [[] for _ in range(len(d))]
    for i, key in zip(range(len(ds)), ds.keys()):
        l[i].append(ds[key])
        l[i].append(key)
    l.sort(key=lambda x: x[0], reverse=True)
    for i in l:
        for _ in range(2):
            try:
                tmp = heapq.heappop(d[i[1]])
                answer.append(tmp[1])
            except BaseException:
                continue
    return answer
