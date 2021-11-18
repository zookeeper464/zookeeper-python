from collections import deque

n,m = map(int,input().split())
mat = [list(input()) for _ in range(n)]
dr,dc = [1,-1,0,0],[0,0,1,-1]
s = 0

for r in range(n):
  for c in range(m):
    if mat[r][c] == '0':
      q = deque([[r,c,0]])

visited = [[[0]*64 for _ in range(m)] for _ in range(n)]
visited[r][c][0] = 1

def check(q):
  cnt = 0

  while q:
    cnt += 1
    for _ in range(len(q)):
      r,c,t = q.popleft()
      for i in range(4):
        nr,nc = r+dr[i],c+dc[i]
        if 0<=nr<n and 0<=nc<m and mat[nr][nc] != '#':
          if mat[nr][nc] == '1':
            return cnt
          
          if mat[nr][nc]>=97:
            if (s>>(ord(mat[nr][nc]-97)))%2:
              q.append()
