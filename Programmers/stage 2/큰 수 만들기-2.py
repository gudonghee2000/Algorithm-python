def solution(number, k):
    queue = []
    i = 0
    rest = ''
    while i < len(number) :
        while queue and queue[-1] < number[i] and k > 0 :
            queue.pop(-1)
            k -= 1
        if k == 0:
            break
        queue.append(number[i])
        i += 1
    while k > 0 :
        queue.pop()
        k -= 1
    return ''.join(queue) + number[i:len(number)]