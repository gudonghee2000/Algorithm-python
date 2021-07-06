def solution(n):
    first = 0
    second = 1
    for i in range(2,n+1) :
        tmp = second
        second = second+first
        first = tmp
    return second%1234567