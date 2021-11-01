def solution(N, stages):
    player = len(stages)
    answer = []
    if N == 1:
        return [1]
    for i in range(1, N+1) :
        fail = 0
        for s in stages :
            if s == i :
                fail += 1
        if fail  == 0:
            answer.append((i, 0))
        else :
            answer.append((i, fail/player))
        player -= fail
    answer.sort(key = lambda x : x[1], reverse=True)
    return [item[0] for item in answer]