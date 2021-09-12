def solution(n):
    one_count = bin(n).count('1')
    while one_count != bin(n+1).count('1') :
        n += 1
    return n + 1