def solution(s):
    s = s.split(' ')
    return ' '.join([i[0:1].upper()+i[1:].lower() for i in s])
