def solution(p, s) :
    day = 0
    a = []
    while p :
        day += 1
        t = 0
        if p[0] + s[0]*day >= 100 :
            while p[0]+ s[0]*day >= 100 :
                del p[0]
                del s[0]
                t += 1
                if not p :
                    break
            a.append(t)
    return a
