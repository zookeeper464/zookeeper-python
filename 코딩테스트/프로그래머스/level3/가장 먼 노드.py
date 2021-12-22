def solution(n, edge):
    from collections import deque
    
    dp = [[] for _ in range(n+1)]
    for a,b in edge:
        dp[a].append(b)
        dp[b].append(a)
    
    visited = [0]*(n+1)
    visited[1] = 1
    q = deque([1])
    
    while q:
        answer = len(q)
        for _ in range(answer):
            node = q.popleft()
            for i in dp[node]:
                if visited[i]: continue
                
                visited[i] = 1
                q.append(i)
                
    return answer