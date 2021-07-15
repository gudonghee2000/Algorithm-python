def solution(n):
    cnt = 0; num = 1
    queue = []
    while num <= n :
        queue.append(num)
        if sum(queue) == n :
            cnt += 1
        while sum(queue) > n :
            queue.pop(0)
            if sum(queue) == n:
                cnt += 1
        num += 1
    return cnt
