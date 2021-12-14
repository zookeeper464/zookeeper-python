def solution(maps):
    def bfs():
        from collections import deque
        nonlocal maps
        
        n,m = len(maps),len(maps[0])
        dr,dc = [1,-1,0,0],[0,0,1,-1]
        q,cnt = deque([[0,0]]),1
        maps[0][0] = 0
        
        while q:
            cnt += 1
            for _ in range(len(q)):
                r,c = q.popleft()
                for i in range(4):
                    nr,nc = r+dr[i],c+dc[i]
                    if 0<=nr<n and 0<=nc<m and maps[nr][nc] == 1:
                        q.append([nr,nc])
                        maps[nr][nc] = 0
                        if (nr,nc) == (n-1,m-1):
                            return cnt
        return -1
    
    answer = bfs()
    
    return answer