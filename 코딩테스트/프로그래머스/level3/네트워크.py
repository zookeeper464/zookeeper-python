from collections import deque
def solution(n, computers):
    answer = 0
    visited = [0 for i in range(n)]
    lst = [[j for j in range(n) if i!=j and computers[i][j]] for i in range(n)]
    for i in range(n):
        if visited[i]: continue
        
        answer += 1
        stack,visited[i] = [i], 1
        while stack:
            x = stack.pop()
            for y in lst[x]:
                if visited[y]: continue
                
                stack.append(y)
                visited[y] = 1
            
    return answer