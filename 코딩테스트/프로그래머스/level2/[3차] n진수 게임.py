def solution(n, t, m, p):
    from collections import deque
    
    answer = ''
    dp = ''
    dic = {i:f'{i}' for i in range(16)}
    for i in range(65,71):
        dic[i-55] = chr(i)
        
    for i in range(t*m):
        if len(dp)>t*m: break
            
        temp,cnt = deque(),i
        while True:
            temp.appendleft(dic[cnt%n])
            cnt //= n
            if cnt == 0: break
        dp += ''.join(list(temp))
    
    for i in range(t):
        answer += dp[i*m+p-1]
        
    return answer