def solution(p, l):
    cnt = 0
    p_index = [i for i in range(len(p))]

    while True:
        if p[0] < max(p):
            p.append(p[0])
            p_index.append(p_index[0])

        else:
            if p_index[0] == l:
                cnt += 1
                break
            cnt += 1

        del p[0]
        del p_index[0]

    return cnt