def solution(citations):
    n = len(citations)
    h = 0
    while True :
        up = 0; down = 0
        for i in citations :
            if h <= i:
                up += 1
        down = n - up
        if h > up or down > h :
            break
        h += 1
    return h-1
