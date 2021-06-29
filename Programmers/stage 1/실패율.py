def solution(N, stages):
    stage = {}
    answer = {}
    l = len(stages)
    for i in range(N):
        stage[i + 1] = 0

    for i in range(len(stages)):
        if stages[i] < N + 1:
            stage[stages[i]] += 1

    for i, j in stage.items():
        if j == 0:
            answer[i] = 0
            continue
        answer[i] = j / l
        l -= j

    a = sorted(answer.items(), key=lambda x: x[1], reverse=True)
    ret = [i[0] for i in a]

    return ret