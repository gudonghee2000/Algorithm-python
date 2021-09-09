def solution(n,a,b):
    count = 1
    if a > b :
        a, b = b, a
    while True :
        if b%2 == 0 and b-a == 1 :
            break
        a = (a+1)//2
        b = (b+1)//2
        count += 1
    return count