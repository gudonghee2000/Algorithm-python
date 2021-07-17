def sum_weight(queue) :
    return sum([i[0] for i in queue])

def solution(b, w, t):
    time = 1
    queue = []
    queue.append([t[0],1])
    del t[0]
    while queue :
        if queue[0][1] == b :
            del queue[0]
        time += 1
        for i in range(len(queue)) :
            queue[i][1] += 1
        if t and sum_weight(queue) + t[0] <= w :
            queue.append([t[0],1])
            del t[0]
    return time
