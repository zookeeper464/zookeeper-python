from collections import deque

n,m = map(int,input().split())
lst = [list(input()) for _ in range(n)]
dp = [[-1 for _ in range(m)] for _ in range(n)]
q = deque([[0,0]])
dr,dc = [1,0,-1,0],[0,1,0,-1]
cnt = 1

while q:
  l = len(q)
  for k in range(l):
    r, c = q.popleft()
    dp[r][c] = cnt
    if (r,c) == (n,m):
      break
    for i in range(4):
      nr, nc = r+dr[i],c+dc[i]
      if 0<=nr<n and 0<=nc<m and lst[nr][nc]=="1" and dp[nr][nc] == -1:
        q.append([nr,nc])
  cnt += 1
  if (r,c) == (n,m):
    break

print(dp[-1][-1])
