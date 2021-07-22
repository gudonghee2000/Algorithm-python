def solution(n, words):
    person = 1
    cnt = 1
    for i in range(len(words)) :
        w = words[i]
        for j in range(i) :
            if w == words[j] :
                return [person, cnt]
        if i >= 1 and words[i-1][-1] != w[0] :
            return [person, cnt]
        person += 1
        if person == n+1 :
            person = 1
            cnt += 1
    return [0,0]
