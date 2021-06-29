def solution(n):
    result = ''
    while n > 0:
        tmp = n % 3
        result += str(tmp)
        n = n // 3

    answer = int(result)
    base = 1
    r = 0

    while answer > 0:
        t = answer % 10
        r += t * base
        base *= 3
        answer = answer // 10

    return r