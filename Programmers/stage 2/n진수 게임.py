def solution(n, t, m, p):
    r = '0'
    alpha = ['A', 'B', 'C', 'D', 'E', 'F']
    num = 1

    while len(r) < t * m:
        z = ''
        prev = num
        while num > 0:
            k = num % n
            if k < 10:
                z += str(k)
            else:
                z += alpha[k - 10]
            num = num // n
        if t * m - len(r) < len(z):
            limit = t * m - len(r)
            r += z[::-1][:limit]
            break
        r += z[::-1]
        num = prev + 1

    return ''.join([r[i] for i in range(p - 1, len(r), m)])
