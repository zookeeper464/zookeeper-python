from collections import deque

n,m = map(int,input().split())
lst = [list(input()) for _ in range(n)]
water_q = deque()
q = deque()
for i in range(n):
  for j in range(m):
    if lst[i][j] == "*":
      water_q.append([i,j])
    elif lst[i][j] == "S":
      q.append([i,j])
dr,dc = [1,0,-1,0],[0,1,0,-1]

def time_rule (water_q,q,answer):
  while q:
    answer += 1
    for _ in range(len(water_q)):
      r,c = water_q.popleft()
      for i in range(4):
        nr,nc = r+dr[i],c+dc[i]
        if 0<=nr<n and 0<=nc<m:
          if lst[nr][nc] =="." or lst[nr][nc] =="S":
            water_q.append([nr,nc])
            lst[nr][nc] = "*"

    for _ in range(len(q)):
      r,c = q.popleft()
      for i in range(4):
        nr,nc = r+dr[i],c+dc[i]
        if 0<=nr<n and 0<=nc<m:
          if lst[nr][nc] ==".":
            q.append([nr,nc])
            lst[nr][nc] = "S"
          elif lst[nr][nc] =="D":
            return answer
  return "KAKTUS"

print(time_rule(water_q,q,0))
