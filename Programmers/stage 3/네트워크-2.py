def dfs(index, visit, computers):
    visit[index] = True
    stack = []
    stack.append(index)
    while stack:
        pos = stack.pop(-1)
        for i in range(len(computers[pos])):
            if pos == i or computers[pos][i] == 0:
                continue
            if visit[i] == False:
                stack.append(i)
                visit[i] = True


def solution(n, computers):
    visit = [False for _ in range(n)]
    cnt = 0

    for i in range(len(visit)):
        if visit[i] == False:
            dfs(i, visit, computers)
            cnt += 1

    return cnt