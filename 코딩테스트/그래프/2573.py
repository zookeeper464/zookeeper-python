from collections import deque

dr = [-1,1,0,0]
dc = [0,0,-1,1]
n,m = map(int,input().split())
lst = [list(map(int,input().split())) for _ in range(n)]

def check (lst,num):
  dp = [[-1]*m for _ in range(n)]
  cnt = 0
  for r in range(n):
    for c in range(m):
      if lst[r][c] > 0 and dp[r][c] == -1:
        q = deque([(r,c)])
        while q:
          tr,tc = q.popleft()
          temp = 0
          for i in range(4):
            nr,nc = tr+dr[i],tc+dc[i]
            if lst[nr][nc] > 0:
              if dp[nr][nc] == -1:
                q.append((nr,nc))
            else:
              temp += 1
          dp[tr][tc] = temp
        cnt += 1
  if cnt == 2:
    print(num)
  elif cnt == 0:
    print(0)
  else:
    lst = water(lst,dp)
    check(lst,num+1)

def water (lst,dp):
  for r in range(n):
    for c in range(m):
      if dp[r][c] > -1:
        lst[r][c] = max(lst[r][c]-dp[r][c],0)
        
  return lst

check(lst,0)
