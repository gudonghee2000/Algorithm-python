def solution(n):
    c = bin(n).count('1')
    while True :
        n = n+1
        if c == bin(n).count('1') :
            return n
