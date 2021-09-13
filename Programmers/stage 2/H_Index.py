def solution(citations):
    ret = 0
    citations.sort()
    for i in range(citations[-1]) :
        H_index = i
        up = 0
        for j in range(len(citations)) :
            if citations[j] >= H_index :
                up += 1
        if up >= H_index and len(citations) - up <= H_index :
            ret = H_index
    return ret