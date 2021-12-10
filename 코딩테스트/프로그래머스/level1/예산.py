def solution(d, budget):
    d.sort()
    
    for idx,v in enumerate(d):
        if budget < v:
            idx -= 1
            break
        budget -= v
        
    answer = idx+1
    
    return answer