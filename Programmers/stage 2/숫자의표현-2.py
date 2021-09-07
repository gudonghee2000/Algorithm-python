def solution(n):
    ret = 0
    queue = []
    for i in range(1, n+1) :
        queue.append(i)
        if sum(queue) == n :
            ret += 1
        elif sum(queue) > n :
            while sum(queue) > n:
                queue.pop(0)
            if sum(queue) == n :
                ret += 1
    return ret