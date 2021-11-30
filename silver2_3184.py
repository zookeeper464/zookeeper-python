from collections import deque

R,C = map(int,input().split())
mat = [list(input().rstrip()) for _ in range(R)]
dr,dc = [1,-1,0,0],[0,0,1,-1]

def bfs (r,c):
    a,b = 0,0
    if mat[r][c] == 'v':
        b += 1
    elif mat[r][c] == 'o':
        a += 1
    mat[r][c] = '#'
    q = deque([[r,c]])

    while q:
        tr,tc = q.popleft()
        for i in range(4):
            nr,nc = tr+dr[i],tc+dc[i]
            if 0<=nr<R and 0<=nc<C and mat[nr][nc] != '#':
                if mat[nr][nc] == 'v':
                    b += 1
                elif mat[nr][nc] == 'o':
                    a += 1
                q.append([nr,nc])
                mat[nr][nc] = '#'
    
    if a>b:
        return a,0
    else:
        return 0,b

sheep,wolves = 0,0
for r in range(R):
    for c in range(C):
        if mat[r][c] != '#':
            a,b = bfs(r,c)
            sheep += a
            wolves += b
            
print(sheep,wolves)