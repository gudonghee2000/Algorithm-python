def gc(first,second) :
    if second == 0 :
        return first
    return gc(second, first%second)

def solution(arr):
    while len(arr) > 1 :
        a = gc(arr[0], arr[1])
        arr.append((arr[0]*arr[1])//a)
        del arr[0:2]
    return arr[0]