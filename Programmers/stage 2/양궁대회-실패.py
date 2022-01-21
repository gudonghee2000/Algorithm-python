max_score = 0
max_info = []


def checkScore(lion, apeach):
    l_score = 0
    a_score = 0
    for i in range(len(lion)):
        if lion[i] > apeach[i]:
            l_score += 10 - i
        elif lion[i] <= apeach[i] and apeach[i] >= 1:
            a_score += 10 - i
    return l_score - a_score


def checker(lion):
    cnt = 0
    for i in range(len(lion)):
        cnt += lion[i]
    return cnt


def dfs(n, cnt, info, result, pos):
    global max_score
    global max_info

    if pos == 10 and checker(result) < n:
        result[pos] = n - checker(result)
        cnt = n
    if n == cnt:
        if checkScore(result, info) >= max_score:
            max_score = checkScore(result, info)
            max_info = list(result)
        return
    if pos > 10:
        return
    new = list(result)
    new[pos] = info[pos] + 1
    dfs(n, cnt + info[pos] + 1, info, new, pos + 1)
    dfs(n, cnt, info, result, pos + 1)


def solution(n, info):
    dfs(n, 0, info, [0] * 11, 0)

    return max_info if max_info != [] else [-1]