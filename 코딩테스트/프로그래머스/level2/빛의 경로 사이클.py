def solution(grid):
    def check(r,c,num):
        nonlocal grid,visited,n,m,dr,dc
        cnt = 0
        while visited[r][c][num]==0:
            cnt += 1
            visited[r][c][num] = 1
            r = (r+dr[num])%n 
            c = (c+dc[num])%m
            if grid[r][c] == 'R': num = (num-1)%4
            elif grid[r][c] == 'L': num = (num+1)%4
        return cnt
    
    n,m = len(grid),len(grid[0])
    dr,dc = [1,0,-1,0],[0,1,0,-1]
    visited = [[[0,0,0,0] for _ in range(m)] for _ in range(n)]
    answer = []
    
    for i in range(n):
        for j in range(m):
            for k in range(4):
                if visited[i][j][k]:
                    continue
                    
                answer.append(check(i,j,k))
    answer.sort()
    return answer