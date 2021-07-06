def solution(n, a, b):
    ret = 0
    while a != b:
        a = (a + 1) // 2
        b = (b + 1) // 2
        ret += 1

    return ret