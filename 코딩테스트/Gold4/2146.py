from collections import deque

def check (r,c):
  global cnt
  cnt += 1
  lst [r][c] = cnt
  q = deque ([[r,c]])
  temp_list = []

  while q:
    r,c = q.popleft()
    temp = 0
    for i in range(4):
      nr,nc = r+dr[i],c+dc[i]

      if 0<=nr<n and 0<=nc<n:
        if lst[nr][nc] == 1:
          if not visited[nr][nc]:
            q.append([nr,nc])
            lst[nr][nc] = cnt
            visited[nr][nc] = True

        else:
          temp = 1
      
    if temp:
      temp_list.append([r,c])

  return temp_list    

def dist(q,num):
  visited = [[False] * n for _ in range(n)]
  distance = 0

  while q:
    for _ in range(len(q)):
      r,c = q.popleft()
      for i in range(4):
        nr,nc = r+dr[i],c+dc[i]

        if 0<=nr<n and 0<=nc<n and not visited[nr][nc]:
          if lst[nr][nc] == 0:
            q.append([nr,nc])
            visited[nr][nc] = True

          elif lst[nr][nc] != num:
            return distance

    distance += 1

    if distance >= answer:
      return answer

dr,dc = [1,-1,0,0],[0,0,1,-1]
answer = 20000
n = int(input())
lst = [list(map(int,input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
dp = [[]]
cnt = 0

for r in range(n):
  for c in range(n):
    if not visited[r][c] and lst[r][c] == 1:
      visited[r][c] = True
      dp.append(check(r,c))

for i in range(1,cnt):
  q = deque(dp[i])
  temp = dist(q,i)
  answer = min(answer,temp)

print(answer)
