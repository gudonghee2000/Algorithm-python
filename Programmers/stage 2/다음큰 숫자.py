def solution(n):
    a = bin(n).count('1')
    b = 0
    while b != a :
        n += 1
        b = bin(n).count('1')
    return n
