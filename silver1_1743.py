from collections import deque

n,m,k = map(int,input().split())
lst = [[0]*m for _ in range(n)]
dr,dc = [1,-1,0,0],[0,0,1,-1]
for _ in range(k):
    r,c = map(int,input().split())
    lst[r-1][c-1] = 1

def check(r,c):
    global answer

    q = deque([[r,c]])
    cnt = 1

    while q:
        for _ in range(len(q)):
            r,c = q.popleft()
            for i in range(4):
                nr,nc = r+dr[i],c+dc[i]
                if 0<=nr<n and 0<=nc<m and lst[nr][nc]:
                    lst[nr][nc] = 0
                    cnt += 1
                    q.append([nr,nc])
    
    if cnt > answer:
        answer = cnt

answer = 0
for r in range(n):
    for c in range(m):
        if lst[r][c] == 1:
            lst[r][c] = 0
            check(r,c)

print(answer)