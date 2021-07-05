from itertools import combinations


def solution(orders, course):
    cnt = 0
    ret = []
    while len(course) > cnt:
        dic = {}
        for k in orders:
            i = sorted(list(k))
            for j in list(combinations(i, course[cnt])):
                if ''.join(j) not in dic:
                    dic[''.join(j)] = 1
                else:
                    dic[''.join(j)] += 1
        dic = sorted(dic.items(), reverse=True, key=lambda x: x[1])

        if dic:
            limit = dic[0][1]
            for i in range(len(dic)):
                if dic[i][1] != limit:
                    break
                if dic[i][1] != 1:
                    ret.append(dic[i][0])
        cnt += 1

    return sorted(ret)