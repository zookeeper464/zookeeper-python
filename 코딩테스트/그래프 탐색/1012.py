import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

t = int(input())
answer = []

def check (r,c):
  global mat
  mat[r][c] = 0
  dr,dc = [0,1,0,-1],[1,0,-1,0]
  for i in range(4):
    nr,nc = r+dr[i],c+dc[i]
    if 0<=nr<n and 0<=nc<m and mat[nr][nc] == 1:
      check(nr,nc)

for _ in range(t):
  m,n,k = map(int,input().split())
  mat = [[0 for _ in range(m)] for _ in range(n)]
  for _ in range(k):
    a,b = map(int,input().split())
    mat[b][a] = 1
  
  cnt = 0
  for r in range(n):
    for c in range(m):
      if mat[r][c] == 1:
        check(r,c)
        cnt += 1
  answer.append(cnt)

for ans in answer:
  print(ans)
