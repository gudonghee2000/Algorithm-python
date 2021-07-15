def solution(prices):
    l = len(prices)
    time = []
    for i in range(l) :
        t = 0
        for j in range(i+1, l) :
            t += 1
            if prices[i] > prices[j] :
                break
        time.append(t)
    return time
