answer = 0


def check(word, begin):
    cnt = 0
    for i in range(len(word)):
        if word[i] != begin[i]:
            cnt += 1
    return True if cnt == 1 else False


def solution(begin, target, words):
    def dfs(begin, target, words, visit, v):
        global answer
        if target == words[v]:
            if answer == 0 or answer > visit.count(True):
                answer = visit.count(True) + 1
        visit[v] = True
        for i in range(len(words)):
            if visit[i] == False and check(words[i], words[v]):
                dfs(words[v], target, words, visit, i)
                visit[v] = False

    for i in range(len(words)):
        if check(words[i], begin):
            visit = [False for _ in range(len(words))]
            dfs(begin, target, words, visit, i)
    return answer

