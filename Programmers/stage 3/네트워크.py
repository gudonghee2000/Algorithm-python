def bfs(visit, coms, c):
    queue = []
    queue.append(c)
    visit[c] = 0
    while (queue):
        q = queue.pop(0)
        for i in range(len(coms[q])):
            if q != i and visit[i] == 1 and coms[q][i] == 1:
                visit[i] = 0
                queue.append(i)


def solution(n, coms):
    if n == 1:
        return 1
    visit = [1 for i in range(n)]
    ret = 0
    for c in range(len(coms)):
        if (visit[c] == 1):
            bfs(visit, coms, c)
            ret += 1
    return ret