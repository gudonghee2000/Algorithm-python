def solution(cacheSize, cities):
    cities = [c.upper() for c in cities]
    time = 0
    cache = []
    for c in cities :
        if c in cache and cacheSize != 0:
            time += 1
            cache.remove(c)
        else :
            time += 5
            if cache and len(cache) >= cacheSize :
                cache.pop()
        cache.insert(0, c)
    return time