def solution(N, stages):
    answer = []
    dp = [0] * (N+2)
    for i in stages:
        dp[i] += 1
    
    lst = []
    child,parent = 0,len(stages)
    for i in range(1,N+1):
        child = dp[i]
        lst.append([i,child/parent])
        parent -= child
        if parent == 0:
            for j in range(i+1,N+1):
                lst.append([j,0])
            break
            
    lst.sort(key = lambda x : (-x[1],x[0]))
    for num,fail in lst:
        answer.append(num)
        
    return answer