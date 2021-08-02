from itertools import combinations

def solution(orders, course):
    answer = []
    cnt = 0
    while cnt < len(course) :
        dic = {}
        for i in orders :
            i = sorted(list(i))
            temp = list(combinations(i,course[cnt]))
            for j in temp :
                if j in dic :
                    dic[j] += 1
                else :
                    dic[j] = 1
        sdic = sorted(dic.items(), key = lambda x : -x[1] )
        if sdic and sdic[0][1] > 1 :
            base = sdic[0][1]
            while sdic and sdic[0][1] == base :
                answer.append(''.join(sdic[0][0]))
                sdic.pop(0)
        cnt += 1
    return sorted(answer)
