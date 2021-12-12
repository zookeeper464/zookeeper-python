def solution(scoville, K):
    from heapq import heappop,heappush,heapify
    
    answer = 0
    heapify(scoville)
    low = scoville[0]
    
    while low < K:
        if len(scoville) <2:
            return -1
        
        a = heappop(scoville)
        b = heappop(scoville)
        answer += 1
        mix = a+2*b
        heappush(scoville,mix)
        low = scoville[0]    
    return answer