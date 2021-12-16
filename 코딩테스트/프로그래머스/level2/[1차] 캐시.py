def solution(cacheSize, cities):
    if cacheSize == 0: return 5*len(cities)
    
    from collections import deque
    
    cities = [i.lower() for i in cities]
    answer = 0
    l = len(cities)
    cache = deque([],maxlen=cacheSize)
    
    for i in cities:
        if i in cache:
            answer += 1
            cache.remove(i)
            cache.append(i)

        else:
            cache.append(i)
            answer += 5
        
    return answer