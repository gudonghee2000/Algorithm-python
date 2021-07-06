def solution(s):
    l = s.split(' ')
    l.sort(key = lambda x : int(x))
    return "{} {}".format(l[0], l[-1])