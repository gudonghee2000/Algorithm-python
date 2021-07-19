def solution(n, t, m, p):
    limit = t * m
    start = 1
    allLine = '0'
    alpha = ['A', 'B', 'C', 'D', 'E', 'F']
    while limit > 0 :
        nowNum = start
        tmp = ''
        while nowNum > 0 :
            r = nowNum%n
            if r >= 10 :
                tmp += alpha[r-10]
            else :
                tmp += str(r)
            nowNum = nowNum//n
            limit -= 1
        start += 1
        allLine += tmp[::-1]
    answerLine = ''
    allLine = allLine[:t*m]
    for i in range(p-1,len(allLine),m) :
        answerLine += allLine[i]
    return answerLine


