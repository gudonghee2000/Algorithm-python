def solution(s):
    s = s.split(' ')
    s.sort(key = lambda x : int(x))
    return s[0] + " " + s[-1]
