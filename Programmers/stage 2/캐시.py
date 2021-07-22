from collections import deque

def solution(cacheSize, c):
    cache = deque()
    time = 0
    if cacheSize == 0 :
        return len(c)*5
    for i in c :
        if i.lower() not in cache :
            if len(cache) < cacheSize :
                cache.appendleft(i.lower())
            else :
                cache.pop()
                cache.appendleft(i.lower())
            time += 5
        else :
            cache.remove(i.lower())
            cache.appendleft(i.lower())
            time += 1
    return time
