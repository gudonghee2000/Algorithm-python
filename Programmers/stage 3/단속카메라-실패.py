def solution(routes):
    routes.sort(key=lambda x: x[0])
    candi = []
    cnt = 0
    print(routes)
    for i in range(len(routes)):
        a, b = routes[i][0], routes[i][1]
        if len(candi) == 0:
            candi.append([a, b])
            continue
        if a <= candi[0][1] and b <= candi[-1][1]:
            candi.append([a, b])
        else:
            cnt += 1
            t_a = candi[-1][1]
            candi = []
            if t_a < a:
                candi.append([a, b])

    return cnt