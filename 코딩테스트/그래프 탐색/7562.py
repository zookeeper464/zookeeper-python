from collections import deque

def bfs (aa,bb,cc,dd):
  if (aa,bb) == (cc, dd):
    return 0
  global chess, n, dr, dc
  q=deque([[aa,bb]])
  cnt = 1
  chess[aa][bb] = cnt
  while q:
    if cnt > 30:
      break
    for _ in range(len(q)):
      r,c = q.popleft()
      if r==cc and c==dd:
        return chess[cc][dd]

      for i in range(8):
        nr,nc = r + dr[i], c + dc[i]
        if 0<=nr<n and 0<=nc<n and chess[nr][nc]==0:
          q.append([nr,nc])
          chess[nr][nc] = cnt
    cnt += 1

answer=[]
t=int(input())
dr=[-2,-2,-1,-1,1,1,2,2]
dc=[1,-1,2,-2,2,-2,1,-1]

for _ in range(t):
  n=int(input())
  aa,bb=list(map(int,input().split()))
  cc,dd=list(map(int,input().split()))
  chess=[[0]*n for i in range(n)]
  answer.append(bfs(aa,bb,cc,dd))
  
for ans in answer:
  print(ans)
