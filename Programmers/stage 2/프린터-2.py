def solution(pri, l):
    answer = 0
    pos = [i for i in range(len(pri))]
    while len(pri) > 1 :
        a = pri.pop(0)
        b = pos.pop(0)
        if max(pri) > a :
            pri.append(a)
            pos.append(b)
        elif b == l :
            break
        else :
            answer += 1
    return answer+1
