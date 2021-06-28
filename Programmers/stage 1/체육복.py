def solution(n, lost, reserve):
    l = list(set(lost) - set(reserve))
    r = list(set(reserve) - set(lost))
    ret = n - len(l)

    for i in range(len(l)):
        if l[i] - 1 in r:
            ret += 1
            r.remove(l[i] - 1)
        elif l[i] + 1 in r:
            ret += 1
            r.remove(l[i] + 1)

    return ret
