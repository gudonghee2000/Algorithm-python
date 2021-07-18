def maxNum(point, nowPos) :
    m = 0
    for i in range(len(point)) :
        if nowPos != i and m < point[i] :
            m = point[i]
    return m

def solution(land) :
    for i in range(1, len(land)) :
        for j in range(len(land[i])) :
            land[i][j] += maxNum(land[i-1], j)
    return max(land[-1])
