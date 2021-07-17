def solution(p, limit):
    p.sort()
    cnt = 0
    start = 0;
    end = len(p) - 1
    while start <= end:
        cnt += 1
        if p[start] + p[end] <= limit:
            start += 1
            end -= 1
        else:
            end -= 1

    return cnt
