def solution(s):
    l = s.split(' ')

    for i in range(len(l)):
        l[i] = l[i].capitalize()

    return ' '.join(l)