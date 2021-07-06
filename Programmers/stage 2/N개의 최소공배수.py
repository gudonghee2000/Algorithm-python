def compare(first, second) :
    m = max(first, second)
    while True :
        if m%first == 0 and m%second == 0 :
            break
        m += 1
    return m

def solution(arr):
    arr.sort()
    m = arr[0]
    for i in range(0, len(arr)-1) :
        m = compare(m, arr[i+1])
    return m