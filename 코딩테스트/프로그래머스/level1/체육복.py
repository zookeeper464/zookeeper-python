def solution(n, lost, reserve):
    dp = [0]*(n+1)
    for i in lost: dp[i] -= 1
    for i in reserve: dp[i] += 1
    
    for i in range(n):
        if dp[i]==-1:
            if dp[i-1]==1: dp[i] = 0
                
            elif dp[i+1]==1: dp[i+1],dp[i] = 0,0
                
    answer = n
    for i in dp:
        if i == -1: answer -= 1
            
    return answer