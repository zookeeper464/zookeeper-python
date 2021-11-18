from collections import deque

n,m = map(int,input().split())
mat = [list(input()) for _ in range(n)]
dr,dc = [1,-1,0,0],[0,0,1,-1]
visited = [[[0]*64 for _ in range(m)] for _ in range(n)]
s = 0

for r in range(n):
  for c in range(m):
    if mat[r][c] == '0':
      mat[r][c] = '.'
      q = deque([[r,c,0]])
      visited[r][c][0] = 1

def check(q):
  cnt = 0

  while q:
    cnt += 1
    for _ in range(len(q)):
      r,c,s = q.popleft()
      for i in range(4):
        nr,nc = r+dr[i],c+dc[i]
        if 0<=nr<n and 0<=nc<m and mat[nr][nc] != '#' and visited[nr][nc][s]==0:
          if mat[nr][nc] == '1':
            return cnt
          
          if ord(mat[nr][nc])>=97:
            temp = 1<<(ord(mat[nr][nc])-97)
            if (s>>(ord(mat[nr][nc])-97))%2==0:
              if not visited[nr][nc][s+temp]:
                q.append([nr,nc,s+temp])
                visited[nr][nc][s+temp] = 1
            else:
              if not visited[nr][nc][s]:
                q.append([nr,nc,s])
                visited[nr][nc][s] = 1

                        
          elif 90>ord(mat[nr][nc])>=65:
            temp = (ord(mat[nr][nc])-65)
            if (s>>temp)%2:
              q.append([nr,nc,s])
              visited[nr][nc][s] = 1

          elif mat[nr][nc] == '.':
            q.append([nr,nc,s])
            visited[nr][nc][s] = 1
  return -1
print(check(q))
