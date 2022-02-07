from collections import defaultdict

answer = set()


def dfs(dic, start, target, time, visit, K):
    global answer
    visit[start] = True

    if time > K:
        return

    if start == target and time <= K:
        answer.add(target)
        return

    for v in dic[start]:
        if visit[v[0]] == False:
            dfs(dic, v[0], target, time + v[1], visit, K)
            visit[v[0]] = False


def solution(N, road, K):
    dic = defaultdict(list)

    for r in road:
        s, e, t = r[0], r[1], r[2]
        dic[s].append([e, t])
        dic[e].append([s, t])

    for n in range(2, N + 1):
        visit = [False for i in range(N + 1)]
        dfs(dic, 1, n, 0, visit, K)

    return len(answer) + 1