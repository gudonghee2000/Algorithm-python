def solution(n,a,b):
    cnt = 1
    if a > b :
        a, b = b, a
    while True :
        if a%2==1 and b%2==0 and a+1 == b :
            break
        a = (a+1)//2
        b = (b+1)//2
        n = n//2
        cnt += 1
    return cnt
