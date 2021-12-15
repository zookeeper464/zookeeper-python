def solution(N, road, K):
    from heapq import heappop,heappush
    
    answer = 0
    time_list = [K+1]*(N+1)
    time_list[1] = 0
    time_roads = [[K+1]*(N+1) for _ in range(N+1)]
    for s,e,t in road:
        time_roads[e][s] = time_roads[s][e] = min(time_roads[s][e],t)
    
    hq = []
    for i in range(1,N+1):
        if time_roads[1][i]<time_list[i]:
            heappush(hq,[time_roads[1][i],i])
            time_list[i] = time_roads[1][i]
    
    while hq:
        t,node = heappop(hq)
        for i in range(1,N+1):
            if time_roads[node][i]+t<time_list[i]:
                heappush(hq,[time_roads[node][i]+t,i])
                time_list[i] = time_roads[node][i]+t
                
    for i in range(1,N+1):
        if time_list[i] <= K:
            answer += 1
            
    return answer