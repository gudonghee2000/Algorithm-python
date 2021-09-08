from itertools import combinations


def solution(orders, course):
    answer = []
    for c in course:
        dic = {}
        for order in orders:
            order = list(combinations(sorted(order), c))
            for o in order:
                if o in dic:
                    dic[o] += 1
                else:
                    dic[o] = 1
        dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)
        max_value = 0
        for key, value in dic:
            if value == 1:
                break
            if max_value == 0 or max_value == value:
                answer.append(key)
                max_value = value
            else:
                break

    return sorted([''.join(a) for a in answer])