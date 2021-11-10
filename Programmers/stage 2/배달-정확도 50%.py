from collections import defaultdict


def dfs(town, start, K, i):
    if i == start:
        return True
    visit = [False for _ in range(len(town) + 1)]
    visit[start] = True
    queue = []
    for t in town[start]:
        if visit[t[0]] == False:
            visit[t[0]] = True
            queue.append([t[0], t[1]])
    while queue:
        n, time = queue.pop(0)
        if time > K:
            continue
        if n == i:
            return True
        for t in town[n]:
            if visit[t[0]] == False:
                visit[t[0]] = True
                queue.append([t[0], t[1] + time])
    return False


def solution(N, road, K):
    cnt = 0
    town = defaultdict(list)
    for r in road:
        town[r[0]].append([r[1], r[2]])
        town[r[1]].append([r[0], r[2]])
    for i in range(1, len(town)):
        town[i].sort(key=lambda x: (x[1]))
    for i in range(1, N + 1):
        if dfs(town, 1, K, i):
            cnt += 1

    return cnt