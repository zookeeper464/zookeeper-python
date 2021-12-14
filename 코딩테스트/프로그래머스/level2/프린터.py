def solution(priorities, location):
    from collections import deque,Counter
    
    dic = Counter(priorities)
    answer = 0
    q = deque([(v,i) for i,v in enumerate(priorities)])

    while q:
        rank = max([i for i,v in dic.items() if v != 0])
        v,idx = q.popleft()
        if rank > v:
            q.append([v,idx])
            continue
        
        answer += 1
        if idx == location:
            break
        dic[v] -= 1
        
    return answer