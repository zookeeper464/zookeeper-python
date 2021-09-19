from collections import deque

n,k = int(input()), int(input())
lst = [[0 for _ in range(n)] for _ in range(n)]
for i in range(k):
  a,b = map(int,input().split())
  lst[a-1][b-1] = 1
dr,dc = [-1,0,1,0],[0,1,0,-1]
look,t = 1,0
l = int(input())
dic = {}
for _ in range(l):
  a,b = input().split()
  if b == 'D': dic[int(a)] = 1
  else: dic[int(a)] = 3

q = deque([[0,0]])
while q:
  t += 1
  r,c = q[-1]
  nr,nc = r+dr[look],c+dc[look]
  if 0<=nr<n and 0<=nc<n:
    if [nr,nc] in q:
      break
    q.append([nr,nc])
    if lst[nr][nc] == 0:
      q.popleft()
    else:
      lst[nr][nc] = 0
  else:
    break
  
  try:
    look = (look+dic[t])%4
  except:
    pass
      
print(t)
