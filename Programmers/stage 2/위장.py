def solution(clothes):
    dic = {}
    answer = 1
    for n, c in clothes :
        if c in dic :
            dic[c] += 1
        else :
            dic[c] = 1
    for i in dic :
        answer *= dic[i]+1
    return answer - 1