def solution(n):
    ret = 0
    while n > 0 :
        if n%2 != 0 :
            n = n-1
            ret += 1
        else :
            n = n//2
    return ret