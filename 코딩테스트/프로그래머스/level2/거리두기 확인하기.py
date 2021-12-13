def solution(places):
    from collections import deque
    def check(mat):
        for r in range(5):
            for c in range(5):
                if mat[r][c] != 'P':
                    continue
                    
                q = deque([[r,c]])
                for _ in range(2):
                    for _ in range(len(q)):
                        tr,tc = q.popleft()
                        for k in range(3):
                            nr,nc = tr+dr[k],tc+dc[k]
                            if 0<=nr<5 and 0<=nc<5 and (r!=nr or c!=nc) and mat[nr][nc] != 'X':
                                if mat[nr][nc] == 'P':
                                    return 0
                                q.append([nr,nc])
        return 1
        
    dr,dc = [1,0,0],[0,1,-1]
    answer = []
    for i in range(5):
        answer.append(check(places[i]))
        
    return answer