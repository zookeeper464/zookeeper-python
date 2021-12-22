def solution(jobs):
    from heapq import heappop, heappush
    
    tasks = sorted([[x[1],x[0]] for x in jobs], key=lambda x:(x[1],x[0]),reverse=True)
    hq = [tasks.pop()]
    t, total = 0, 0
    
    while hq:
        dur, arr = heappop(hq)
        t = max(t,arr)+dur
        total += t - arr
        
        while tasks and tasks[-1][1] <= t:
            heappush(hq, tasks.pop())
            
        if tasks and not hq:
            heappush(hq, tasks.pop())
            
    answer = total//len(jobs)
    
    return answer