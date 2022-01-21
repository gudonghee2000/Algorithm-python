from collections import defaultdict


def solution(id_list, report, k2):
    dic = defaultdict(list)
    dic2 = {}
    for i in id_list:
        dic2[i] = 0
    for r in report:
        a, b = r.split(" ")
        if a not in dic[b]:
            dic[b].append(a)

    for k, v in dic.items():
        if len(v) >= k2:
            for ll in v:
                dic2[ll] += 1

    return [v for v in dic2.values()]